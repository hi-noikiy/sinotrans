
用户的扩展要涉及的以下几个方面:
- 用户数据扩展
- 用户授权

djangoproject - [topics-auth](https://docs.djangoproject.com/en/dev/topics/auth/default)


# 基本用户 (django 实现)
## 模型定义
``` python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

```

上面是当前django的用户定义，User从AbstractUser继承而来。
abstract = True，所以AbstractUser是抽象类，不能实例化

## 用户授权 authenticate
当项目调用authenticate时，它会直接调用这个函数

django.contrib.auth.\__\init\_\_

``` python
def authenticate(**credentials):
    """
    If the given credentials are valid, return a User object.
    """
    for backend, backend_path in _get_backends(return_tuples=True):
        try:
            inspect.getcallargs(backend.authenticate, **credentials) # 遍历backend
        except TypeError:
            # This backend doesn't accept these credentials as arguments. Try the next one.
            continue
 
        try:
            user = backend.authenticate(**credentials) # 调用backend的authenticate函数
        except PermissionDenied:
            # This backend says to stop in our tracks - this user should not be allowed in at all.
            return None
        if user is None:
            continue
        # Annotate the user object with the path of the backend.
        user.backend = backend_path
        return user
 
    # The credentials supplied are invalid to all backends, fire signal
    user_login_failed.send(sender=__name__,
            credentials=_clean_credentials(credentials))
```
1. inspect.getcallargs(backend.authenticate, **credentials)

首先它会遍历backend，根据参数去找到合适的authenticate函数，这个backend在settings.py文件AUTHENTICATION_BACKENDS里定义。

2. user = backend.authenticate(**credentials)

当authenticate函数找到之后，它就会接下来执行授权操作，并返回用户信息

### backend
backend的实现可以参考下面的例子

django.contrib.auth.backends.py
``` python
class ModelBackend(object):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """
 
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)
``` 
如果函数调用authenticate(username, password)或者authenticate(email, password)(如何email是USERNAME_FIELD)，那么该backend会被调用

### 参考文档
[1] https://docs.djangoproject.com/en/dev/topics/auth/customizing/#writing-an-authentication-backend

demo代码里backend的authenticate的参数包含request，调用authenticate时，必须request=request, 
否则django.contrib.auth.__init__的```authenticate(**credentials)```函数在getcallargs这一步会出错，因为request这个参数不能传进```**credentials```

学到这儿的时候对Keyword Arguments理解还不够，刚好学习了一下，可以看一下下面文档
- [Keyword Arguments](https://docs.python.org/2/tutorial/controlflow.html#keyword-arguments)
- [python 中参数*args, **kwargs](http://blog.csdn.net/anhuidelinger/article/details/10011013)

## 登陆 login

__init__.py (site-packages\django\contrib\auth)

``` python
SESSION_KEY = '_auth_user_id'
BACKEND_SESSION_KEY = '_auth_user_backend'
HASH_SESSION_KEY = '_auth_user_hash'
REDIRECT_FIELD_NAME = 'next'
 
def login(request, user):
    """
    Persist a user id and a backend in the request. This way a user doesn't
    have to reauthenticate on every request. Note that data set during
    the anonymous session is retained when the user logs in.
    """
    session_auth_hash = ''
    if user is None:
        user = request.user
    if hasattr(user, 'get_session_auth_hash'):
        session_auth_hash = user.get_session_auth_hash()
 
    if SESSION_KEY in request.session:
        if _get_user_session_key(request) != user.pk or (
                session_auth_hash and
                request.session.get(HASH_SESSION_KEY) != session_auth_hash):
            # To avoid reusing another user's session, create a new, empty
            # session if the existing session corresponds to a different
            # authenticated user.
            request.session.flush()
    else:
        request.session.cycle_key()
 
# 正常用户登录时，会保存这个用户session，这样在response的消息里的request里面会带出去user信息
    request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
    request.session[BACKEND_SESSION_KEY] = user.backend
    request.session[HASH_SESSION_KEY] = session_auth_hash
    if hasattr(request, 'user'):
        request.user = user
    rotate_token(request)
    user_logged_in.send(sender=user.__class__, request=request, user=user)

```
1. request.session[SESSION_KEY] = user.\_meta.pk.value_to_string(user)  
SESSION_KEY会在后面_get_user_session_key中使用，用于获取用户
2. request.session[BACKEND_SESSION_KEY] = user.backend  
如果授权成功，django会把这个授权方式保存到session里，session周期里的下一次接入还是用这种方式。如果要强迫用不同方法授权，一个简单的方法是调用Session.objects.all().delete()

注意两个user的差别
``` html
{{user}}
{{request.user}}
 ```
这两个user分别是由下面的middleware传进来的
``` python
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
```


## context_processors
django.contrib.auth.context_processors.auth
``` python
def auth(request):
    """
    Returns context variables required by apps that use Django's authentication
    system.
 
    If there is no 'user' attribute in the request, uses AnonymousUser (from
    django.contrib.auth).
    """
    if hasattr(request, 'user'):
        user = request.user
    else:
        from django.contrib.auth.models import AnonymousUser
        user = AnonymousUser()
 
    return {
        'user': user,
        'perms': PermWrapper(user),
    }
``` 
user赋值在这儿完成，如果是非登陆用户，则为AnonymousUser

## middleware

Middleware.py (site-packages\django\contrib\auth
``` python
def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
return request._cached_user
 
class AuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE_CLASSES setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        )
        request.user = SimpleLazyObject(lambda: get_user(request))
``` 

## 获取用户 get_user
系统里多个地方都调用了get_user

跟authenticate类似，它也会轮询多个backend找到对应的函数

django/contrib/auth/__init__
``` python
def get_user(request):
    """
    Returns the user model instance associated with the given request session.
    If no user is retrieved an instance of `AnonymousUser` is returned.
    """
    from .models import AnonymousUser
    user = None
    try:
        user_id = _get_user_session_key(request) 
        backend_path = request.session[BACKEND_SESSION_KEY]
    except KeyError:
        pass
    else:
        if backend_path in settings.AUTHENTICATION_BACKENDS:
            backend = load_backend(backend_path)
            user = backend.get_user(user_id)
            # Verify the session
            if ('django.contrib.auth.middleware.SessionAuthenticationMiddleware'
                    in settings.MIDDLEWARE_CLASSES and hasattr(user, 'get_session_auth_hash')):
                session_hash = request.session.get(HASH_SESSION_KEY)
                session_hash_verified = session_hash and constant_time_compare(
                    session_hash,
                    user.get_session_auth_hash()
                )
                if not session_hash_verified:
                    request.session.flush()
                    user = None
 
    return user or AnonymousUser()
```

- (1) \_get_user_session_key(request)
SESSION_KEY在login中赋值了

django/contrib/auth/backends.py
``` python
class ModelBackend(object):    
    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
```

django/contrib/auth/forms.py
``` python
class AuthenticationForm(forms.Form):
    def get_user(self):
        return self.user_cache
```

django/contrib/auth/middleware.py
``` python
def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
    return request._cached_user
```


## 应用调用
https://docs.djangoproject.com/en/dev/topics/auth/default/#how-to-log-a-user-in
``` python 
from django.contrib.auth import authenticate, login
 
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request= request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
```

# 用户扩展 (支持电话号码)
用户扩展包括以下几种方法
- (1) 直接修改django 源码 
- (2) 把django 的user以及认证部分的源代码拷贝到自己的app下面
- (3) OneToOneField扩展
- (4) Profile Model (1.5之后不再支持)
- (5) AbstractBaseUser, PermissionsMixin开始派生出一个自定用户Model，并且实现自定义的BaseUserManager (1.5之后)
- (6) ProfileBase(type)
- (7) 继承User

(1)(2)，每次升级之后都要修改，维护成本太高  
(3) 这个在原始的用户扩展中一般不用，因为会增加新的Models，但是对于额外的用户信息一般采用这种方法，比如微信用户，支付用户等等  
(4) 不再支持  
(5) 本文会采用该方法  
(7) 从它的基类继承会更灵活  

## 添加用户域
新的用户域如下

| Field	| Type	| Property | Description |
|-------|-------|----------|:-------------|
|username	| CharField	| unique |	用户名 [如果电话注册= phone]
|phone |	CharField	| |	电话
|first_name	| CharField	| |	名
|last_name	| CharField	| |	姓
|email	| EmailField	| |	邮箱
|sex	| CharField		| | 性别
|birthday	| DateField	| |	生日
|nickname	| CharField	| |	昵称
|image	| ImageField	| |	头像
|is_staff	| BooleanField |	| 职员状态 指明用户是否可以登录到这个管理站点。<br> Boolean. Designates whether this user can access the admin site.
|is_super	| BooleanField	| |	超级用户状态 指明该用户缺省拥有所有权限。<br> Boolean. Designates that this user has all permissions without explicitly assigning them.
|is_active	| BooleanField	| |	有效 <br> 指明用户是否被认为活跃的。以反选代替删除帐号。 <br>Boolean. Designates whether this user account should be considered active. Set this flag to False instead of deleting accounts.
|date_joined	| DateTimeField	| | 加入时间
|account_type	| CharField	| | [mail, phone]	注册类型
			

authwrapper\models.py
``` python
from __future__ import unicode_literals
from authwrapper.fields import EmailNullField, PhoneNumberNullField
from authwrapper.validators import (ASCIIUsernameValidator,
                                    UnicodeUsernameValidator)
                                    
class MyUser(MyAbstractUser):
    class Meta(MyAbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class MyAbstractUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    username = models.CharField(_('username'), 
        max_length=30, 
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),                    
        #validators=[
        #    validators.RegexValidator(r'^[\w.@+-]+$',
        #                              _('Enter a valid username. '
        #                                'This value may contain only letters, numbers '
        #                                'and @/./+/-/_ characters.'), 'invalid'),
        #],        
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    email = EmailNullField(_('email address'), max_length=255,null=True, blank=True, unique=True)
    phone = PhoneNumberNullField(_('phone'), max_length=30, blank=True, unique=True,
        help_text=_('Required. digits and + only.'),
        error_messages={
            'unique': _("A user with that phone number already exists."),
        })
        
    account_type = models.CharField(max_length=50, blank=True, null=True, choices=USER_TYPE, default = 'username') #login account type

    USERNAME_FIELD = 'phone' if 'phone' == settings.ACCOUNT_REGISTER_TYPE  else 'username'
    REQUIRED_FIELDS = ['email'] if 'phone' == settings.ACCOUNT_REGISTER_TYPE  else ['phone','email']
    
    objects = MyUserManager()
 
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True
```

1. 添加新的filed **phone**
- 首先安装库django-phonenumber-field
- PhoneNumberNullField从PhoneNumberField继承而来，当内容为空时保存为Null
- phone number的validation会在这个field内完成

2. 扩展EmailField为EmailNullField

3. 添加Username的validator，支持py3和py2
下面这句话是为了兼容py3
``` python
from __future__ import unicode_literals
```

4. 在settings.py里添加配置ACCOUNT_REGISTER_TYPE，指示默认注册方式是邮件还是电话号码

5. 根据ACCOUNT_REGISTER_TYPE确定USERNAME_FIELD和REQUIRED_FIELDS

6. swappable = 'AUTH_USER_MODEL'
> swappable is an "intentionally undocumented" feature which is currently under development / in-test. It's used to handle "I have a base abstract model which has some foreign-key relationships." Slightly more detail is available from [Django's ticketing system](https://code.djangoproject.com/ticket/19103) and [github](https://github.com/wq/django-swappable-models). Because it's a "stealth alpha" feature, it's not guaranteed to work (for anything other than User), and understanding the detailed operation will likely require diving into source code. It works with AUTH_USER_MODEL because the User model and swappable flag were developed together, specifically for each other.

## 修改AUTH_USER_MODEL
在settings.py添加
``` python
AUTH_USER_MODEL = 'authwrapper.MyUser'
```
以后调用新用户时，可以用django.contrib.auth.get_user_model或者settings.AUTH_USER_MODEL

## 信号
django系统里面username是默认存在，如果用电话号码注册，这个信息一开始并不是必须的，为了通过django的验证，暂时通过设置username=phone来保证models的validation

authwrapper\models.py
``` python
def myuser_pre_save_receiver(sender, instance, *args, **kwargs):
    if 'phone' == MyUser.USERNAME_FIELD:
        if instance.username is None: # hide username and copy value from phone number
            instance.username = instance.phone
```
pre_save.connect(myuser_pre_save_receiver, sender=MyUser)

## 添加用户及管理
authwrapper\models.py
``` python
    def _create_user(self, username, email, phone, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, 
                          email=email,
                          phone=phone,
                          date_joined=now, 
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
class MyUserManager(BaseUserManager):
    def create_user(self, username, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, phone, password, **extra_fields)

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if 'phone' == settings.ACCOUNT_REGISTER_TYPE:
            #{'phone': '13500000000', u'password': '123', 'email': '', 'sex': 'male'}
            #get usename from phone, and unpack the rest
            return self._create_user(extra_fields.get('phone'), account_type='phone',
                                 **extra_fields)
        else:
            return self._create_user(account_type='mail',
                                 **extra_fields)
                                 
```
跟基本的class UserManager(BaseUserManager):相比，做了一下的修改
1. \_create_user里面将is_superuser和is_staff从入参里面去掉，合进了extra_fields，调用更灵活
2. create_superuser里面把所有的显示参数都去掉了，放进了extra_fields，改动的原因是如果不这么修改，执行```python manage.py createsuperuser```时会报参数缺失的错误，这个函数的实现中，username会copy phone的值。
下一步是修改django\contrib\auth\management\commands\createsuperuser.py，可以指定函数参数

# 扩展用户授权
用户授权的实现包括以下几个方面
- 在settings.py添加backend入口
- 实现backend完成authenticate工作

## 指定authentication backend
Django维护了一个“authentication backends”列表，通过它在授权。Django会遍历所有的backends直到授权接收。
authentication backends在settings里的[AUTHENTICATION_BACKENDS](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-AUTHENTICATION_BACKENDS)指定，可以是任意路径，默认的backends是
```['django.contrib.auth.backends.ModelBackend']```  
轮询算法见authenticate
 
AUTHENTICATION_BACKENDS的顺序是有影响的，如果多个backends的用户名和密码都能验证通过，django在第一次匹配后就会停止。所以要特别小心参数的匹配。  
如果backend抛出[PermissionDenied](https://docs.djangoproject.com/en/dev/ref/exceptions/#django.core.exceptions.PermissionDenied)异常，授权检查会立即停止，不会再检查后面的backend。
 
**注意**：如果授权成功，django会把这个授权方式保存到session里，session周期里的下一次接入还是用这种方式。如果要强迫用不同方法授权，一个简单的方法是调用Session.objects.all().delete().
 
Settings.py
``` python
AUTHENTICATION_BACKENDS = (        
    'authwrapper.backends.auth.MyBackend', 
    'django.contrib.auth.backends.ModelBackend', 
    )
AUTH_USER_MODEL = 'personalcenter.MyUser'
```

## 实现authentication backend
必须实现的方法
``` python
get_user(user_id)
authenticate(request, **credentials)
```

遗留问题
> 不知道为什么？username登录时的request.user是有值的，但是wechat登录永远是anonymous，这个从一开始的render就开始了
\_cached_user为AnonymousUser: AnonymousUser  
>问题查清楚了，下面这个wechat auth backend函数没写好，之前返回None，这个函数在eclipse上打断点也进不去不知道为什么  
>好像也不是这个问题，突然就好了

authwrapper\backends\auth.py
``` python
class MyBackend(object):
    """Allows user to sign-in using email, username or phone_number."""
    def authenticate(self, username=None, password=None, **kwargs):  
        try:
            """login with user info directly"""
            if kwargs['user'] :
                if isinstance(kwargs['user'], UserModel):
                    return kwargs.get('user',None)
                else: 
                    return None
        except:
            pass

        user = None
        if username is None and kwargs.get(UserModel.USERNAME_FIELD,None) is None:
            return None
            
        try:
            """if allow mix login options
            username/phone/mail """
            if True == settings.ACCOUNT_ALLOW_MIX_TYPE_LOGIN:
                if '@' in username:
                    user = UserModel._default_manager.get(email=username)
                elif '+' in username[0]: # to be precise
                    user = UserModel._default_manager.get(phone=username)
                else:
                    user = UserModel._default_manager.get(username=username)
            else:    
                user = UserModel._default_manager.get_by_natural_key(username)
            
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            else:
                return None
                
    def user_can_authenticate(self, user):
        """Reject users with is_active=False. Custom user models that don't have that attribute are allowed."""
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None
        
    def get_user(self, user_id):        
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None        
            
```    
1. authenticate
这里面包含了几种场景
- 传递user信息，那么如果用户存在的话，可以直接授权，这个往往用于第三方授权场景。第三方本身授权通过之后，然后储存的信息获取到MyUser信息，然后执行授权，不执行授权login会失败
- 混合输入登陆，支持用户名，电话，邮箱登陆，这个时候要尝试多种匹配
- 单一登陆，根据setting设置的登陆方式进行校验授权

2. get_user
获取用户信息

3. user_can_authenticate
这个用于验证注册的场景，比如邮箱或者电话号码注册账号都会立即创建账户，但不会立即激活，只有激活is_active = True之后，才能授权

4. UserModel.\_default_manager.get和UserModel.\_default_manager.get_by_natural_key
``` python
user = UserModel.objects.filter(username=username).first()  
user = UserModel.objects.get(username=username) 
```
上面这两种方式调用都会出错，分析原因可能是因为UserModel有多个manager, 导致行为上有差异，待验证
> UserModel.\_default_manager
> MyUserManager: personalcenter.MyUser.objects

> UserModel.\_base_manager
> Manager: personalcenter.MyUser.\_base_manager

以后关于UserModel的get，尽量用 UserModel._default_manager

针对不同的注册方式，get_by_natural_key可能根据 USERNAME_FIELD 准确的找到默认的field

``` python
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})
```	
\*\*{}解决了get后面model名字不确定的问题，也是之前困扰voith的一个问题

执行get时会做validation，即使值一致但是validation不过也会返回失败  
比如电话号码+86135000000000，之前validation时没有+86，添加的值也不会带+86.  
Validation规则变化之后，即使搜索135000000000（老的添加值在数据库存在）也会返回失败

# 用户扩展 (支持微信)
这儿会用到一个微信库 [python-weixin](https://pypi.python.org/pypi/python-weixin)

1. 定义微信用户数据模型

authwrapper\models.py
``` python
class WechatUserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    openid = models.CharField(max_length=120, blank=True, null=True) #wechat only
    unionid = models.CharField(max_length=120, blank=True, null=True) #wechat only
    privilege = models.CharField(max_length=120, blank=True, null=True) #wechat only    
    headimgurl = models.CharField(max_length=500, blank=True, null=True)
    nickname = models.CharField(max_length=120, blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)    
    city = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)    
    language = models.CharField(max_length=45, blank=True, null=True)

    def __unicode__(self):
        if self.nickname:
            return self.nickname
        elif self.user:
            return self.user.username
        else:
            return self.openid

    def get_absolute_url(self):
        return reverse("personalcenter", kwargs={"id": self.id })  

    def get_image_url(self):
        return self.headimgurl   
```
这些域field是从微信的结构拷贝来的，添加了OneToOneField user

2. 添加backend (settings.py)
``` python
AUTHENTICATION_BACKENDS = (    
    'authwrapper.backends.auth.WechatBackend',
    )
```

3. 实现backend
同样要实现基本的authenticate和get_user函数

authwrapper\backends\auth.py
``` python
class WechatBackend(object):

    def authenticate(self, request, user):
        obj = None
        cur_user = auth.get_user(request)
        profile, created = WechatUserProfile.objects.get_or_create(openid = user['openid'])

        if created is False:
            obj = profile.user            
            if profile.user is None: # wechat profile not linked to UserModel yet
                 if cur_user.is_active and not cur_user.is_anonymous() and cur_user is not None:
                    profile.user =  cur_user # link wechat profile to UserModel
                    profile.save()
        else:
            profile.unionid = user['unionid']
            #profile.privilege = user['privilege'] #privilege is list
            profile.city = user['city']
            profile.country = user['country']
            profile.language = user['language']
            if 1 == user['sex']:
                profile.sex = 'male'
            else:
                profile.sex = 'female'
            profile.nickname = user['nickname']
            profile.headimgurl = user['headimgurl']
            if cur_user.is_active and not cur_user.is_anonymous() and cur_user is not None:
                profile.user = cur_user
            profile.save()
            obj = request.user

        request.session['wechat_id'] = profile.id
        # request._cached_user = obj

        return obj

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
```	    
1. authenticate
调用时传递的参数为request和user，这个user是WeixinMpAPI User
 
根据openid获取wechat用户model, 如果该wechat用户已存在，进一步检查该用户是否已关联UserModel，如果未关联，则关联数据；如果wechat用户不存在，则创建新用户

2. get_user
该处返回的还是UserModel对象

3. get_wechat_user
django在维护user的信息，但是wechat user的信息，需要我们自己维护  
目前的实现方式是通过添加session "wechat_id"在完成的，授权完成之后
``` python
request.session['wechat_id'] = profile.id
```
定义 get_wechat_user 用于获取wechat用户
``` python
    def get_wechat_user(self, request):
        wechat_id = request.session.get("wechat_id", None)
        if wechat_id:
            try:
                wechat = WechatUserProfile.objects.get(pk=wechat_id)
                return wechat
            except:
                pass
        return None
```
在middle里将wechat信息添加进request，这样在处理navbar登陆选项时能够知道wechat信息

zakkabag\middleware.py
``` python
class openidmiddleware():

	def process_request(self, request):
		request.register_type = settings.ACCOUNT_REGISTER_TYPE
		    		    
		if request.user.is_anonymous:
		       from django.utils.module_loading import import_string
		       backend = import_string('authwrapper.backends.auth.WechatBackend')()
		       request.wechat = backend.get_wechat_user(request)
```

学习get_user里面load module的方法 - load_backend，里面用了一个新的方法去import model (import_string)，可以以后再函数里对module数组操作时使用，这儿仅是一个练习

调用get_wechat_user的必须是一个函数，所以要对它实例化之后才能调用

logout的时候要删除这个session
``` python
del request.session['wechat_id']
```

## 登陆 login
```
from django.contrib.auth import login as auth_login
```
登陆最终都会调用基本的login函数


## 退出   
``` python
from django.contrib.auth import logout as auth_logout

def logout(request):
    try:
        del request.session['wechat_id']
    except:
        pass
    auth_logout(request)
    return redirect(reverse("home", kwargs={}))
```
退出时调用基本的logout函数，并删除wechat_id session

## 完整的过程
authwrapper\login.py
```
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_views
def login(request):
    REDIRECT_URI = request.POST.get('next', request.GET.get('next', reverse("home", kwargs={}))) #next indicated in templaetes
    if request.method == 'GET':
        code = request.GET.get('code')
        if code:
            redirect_to = "http://%s%s" % (request.META['HTTP_HOST'], reverse("home", kwargs={})) # redirection URL after authenticate
            api = WeixinMpAPI(appid=APP_ID, 
                        app_secret=APP_SECRET,
                        redirect_uri=redirect_to)
            auth_info = api.exchange_code_for_access_token(code=code)
            api = WeixinMpAPI(access_token=auth_info['access_token'])
            api_user = api.user(openid=auth_info['openid'])                
            user = authenticate(request = request, user = api_user)
            if user and not user.is_anonymous():
                auth_login(request, user)
                return redirect(redirect_to)

        return redirect(reverse("auth_login", kwargs={})) # if user is not login, redirect to login template
    else:  #normal login is POST
        REDIRECT_FIELD_NAME = 'next'
        return auth_views.login(request, redirect_field_name=REDIRECT_FIELD_NAME, extra_context=None)    

    return auth_views.login(request, redirect_field_name=REDIRECT_URI, extra_context=None)    
```
1. WeixinMpAPI对微信进行授权

登陆的过程会用到python-weixin的API，这个API主要是针对Mobile Phone使用的，其实的还没有去尝试使用过
其中会用到几个参数APP_ID，APP_SECRET，这些都可以在公众号里面获取  
redirect_uri表示授权成功之后跳转的地址  
Wechat的login是通过get方式进行的

2. 系统授权

对于微信登陆方式，授权传递的参数即为wechat profile，在authenticate函数里会把它和UserModel进行绑定处  
- 如果当前用户已登陆，则直接绑定该用户到微信账户，将来可能会增加确认窗口 (WechatBackend.authenticate)
- 否则重定向到新的网页进行登陆或注册处理，登陆或注册成功后会继续绑定

提取上面的部分代码，如果用户存在，并且非匿名用户，说明wexin登陆之前，用户已正常登陆，并且在authenticate里面已完成绑定。否则，重定向到登陆界面
```
if user and not user.is_anonymous():
    auth_login(request, user)
    return redirect(redirect_to)
return redirect(reverse("auth_login", kwargs={}))
```

登陆的模板如下，用户登陆成功时进行绑定

templates\registration\login.html
``` html
{% block content %}
<div class = "row">
    <div class = "col-sm-3 col-sm-offset-3">

        {% if request.user.is_anonymous and request.wechat %}
            You need to login to continue
        {% endif %}
        
        <form method="post" action=""> {% csrf_token %}
            
            {{ form|crispy }}
            
            <input class = "btn btn-block btn-primary" type="submit" value="{% trans 'Log in' %}" />
            
            {% if request.user.is_anonymous and request.wechat %}
                <input type="hidden" name="next" value="{% url 'link_to_wechat' %}" /> 
	        <!-- workaround here, maybe we need to change it in login function later-->
            {% else %}
                <input type="hidden" name="next" value="{{ next }}" /> 
            {% endif %}
        </form>
        
    </div>
</div>
{% endblock %}
```
next跳转链接会根据用户状态进行设置，如果发现系统用户未登陆，但微信用户登陆了，则在提交成功后重定向到link_to_wechat进行关联

注册情况下的处理，最终激活成功时进行绑定

templates.registration.activation_complete.html
``` html
{% block content %}
<p class = "lead">
    {% trans "Your account is now activated." %}
    {% if not user.is_authenticated %}
    	{% trans "You can log in." %}
    {% else %}
    	<a href='{% url "link_to_wechat" %}'>Link to wechat</a> 
    {% endif %}
</p>
{% endblock %}
```

personalcenter\login.py
``` python
@login_required
def account_link_to_wechat(request):
    user = auth.get_user(request)
    wechat = WechatBackend().get_wechat_user(request)
    if wechat:
        wechat.user = user   
        wechat.save()    
        return redirect(reverse("home", kwargs={}))

    return redirect(reverse("home", kwargs={}))
```    

对于正常登陆方式，可以针对不同的backend进行授权
比如：
- ModelBackend
``` python
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
```

3. 登陆

最终的登陆都是调用django.contrib.auth.login
- django.contrib.auth.login() 纯登陆操作，之前需完成相关的授权工作

有些情况可以把调用封装起来，比如login form的处理
- django.contrib.auth.view.login()，这个是正常的视图的登陆的处理，模板为'registration/login.html'

	    
## 参考文档
1. https://docs.djangoproject.com/en/1.5/ref/settings/#auth-profile-module 
2. https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
3. [Django中扩展User模型](http://blog.csdn.net/watsy/article/details/15506351)
4. [非profile方式扩展Django User Model](http://onlypython.group.iteye.com/group/wiki/1519-expansion-django-user-model-by-non-profile-way)
5. [django user 权限](http://www.cnblogs.com/smallcoderhujin/p/3193103.html)
6. [django 注册、登录及第三方接口程序(2)：扩展User表](http://www.tuicool.com/articles/aMBJNjj)
7. [扩展django的User的部分方法](http://www.cnblogs.com/captain-cp/p/3590213.html)
8. [django admin框架使用系列之三:扩展user model](http://www.yihaomen.com/article/python/334.htm）
9. [Django扩展user表并使用email登陆](http://www.python88.com/topic/395/)
10. [Django 扩展 User model 的字段有什么好的方法？](https://segmentfault.com/q/1010000000610904)
11. [django使用email进行身份验证](http://guangboo.org/2013/03/27/authentication-using-email-in-django)
12. [自定义的用户认证如何登录使用Django自带的后台管理?](https://www.oschina.net/question/2341837_235437)




# 用户扩展 (支持头像)

# 用户注册 （邮箱）

# 用户注册 （手机）

# 登陆后跳转
登录成功或者密码修改成功之后，跳转回原来的网址或者指定的地址

以admin的auth为例：  
在template里面定义好’next’网址，并通过GET/POST方法传递给后台，后台在login成功之后会重定向到该网址
有时需要获取当前site网址，可以使用get_current_site方法

__init__.py (site-packages\django\contrib\auth)
``` python
REDIRECT_FIELD_NAME = 'next'
```
Views.py (site-packages\django\contrib\auth)
``` python
@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)

```
redirect_to变量的赋值顺序
- POST['next']
- settings.LOGIN_REDIRECT_URL

顺便讲一下这儿获取网址用到了get_current_site去获取完整域名，有的地方也用了request.META.get('HTTP_REFERER')去获取带域名网址

Shortcuts.py (site-packages\django\contrib\sites)
``` python
def get_current_site(request):
    """
    Checks if contrib.sites is installed and returns either the current
    ``Site`` object or a ``RequestSite`` object based on the request.
    """
    # Imports are inside the function because its point is to avoid importing
    # the Site models when django.contrib.sites isn't installed.
    if apps.is_installed('django.contrib.sites'):
        from .models import Site
        return Site.objects.get_current(request)
    else:
        from .requests import RequestSite
        return RequestSite(request)
```

Models.py (site-packages\django\contrib\sites)
``` python
class SiteManager(models.Manager):
     def get_current(self, request=None):
        """
        Returns the current Site based on the SITE_ID in the project's settings.
        If SITE_ID isn't defined, it returns the site with domain matching
        request.get_host(). The ``Site`` object is cached the first time it's
        retrieved from the database.
        """
        from django.conf import settings
        if getattr(settings, 'SITE_ID', ''):
            site_id = settings.SITE_ID
            return self._get_site_by_id(site_id)
        elif request:
            return self._get_site_by_request(request)

        raise ImproperlyConfigured(
            "You're using the Django \"sites framework\" without having "
            "set the SITE_ID setting. Create a site in your database and "
            "set the SITE_ID setting or pass a request to "
            "Site.objects.get_current() to fix this error."
        )
```

应用举例：

Login.html (site-packages\registration\templates\registration)
``` html
<form method="post" action="">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="{% trans 'Log in' %}" />
    <input type="hidden" name="next" value="{{ next }}" />
</form>
```
该next值会传递给login函数



