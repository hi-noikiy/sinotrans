# 日历控件

admin site 中的日历控件使用方法很简单
``` html
<input type="text" class="vDateField">
<input type="text" class="vTimeField">
```
只要页面中的 input 的 class 属性为 vDateField 或者 vTimeField 即可，会自动在输入框后边添加上日历控件开关，这两个 class 属性一个选择是日期控件一个是选择时间控件（注意这里设置的 input type 为 text 和标准的 date 值不同）

接下来是载入控件所需要的资源

css 资源
templates\admin_css.html

``` javascript
<link rel="stylesheet" type="text/css" href="{% static 'admin/css/base.css' %}" />
<link rel="stylesheet" type="text/css" href="{% static 'admin/css/forms.css' %}" />
```
注意这些 css 资源包含了太多其它 admin site 中使用的 css 样式，请确保在你页面其它css资源前载入，否则会覆盖掉你页面中原先的样式。

js 资源
``` javascript
<script src="/admin/jsi18n/"></script>
<script src="{% static 'admin/js/core.js' %}"></script>

<script src="{% static 'admin/js/jquery.init.js' %}"></script>

<script src="{% static 'admin/js/calendar.js' %}"></script>
<script src="{% static 'admin/js/admin/DateTimeShortcuts.js' %}"></script>
<script type="text/javascript">window.__admin_media_prefix__ = "{% filter escapejs %}{% static 'admin/' %}{% endfilter %}";</script>
```

参考文档里提到的下面这个文件没找到
``` javascript
<script src="{% static 'admin/js/jquery.init.both.js' %}"></script>
```

这个 jsi18n 是需要专门在 urls.py 设定的，如果不设置那么访问不了admin site 的用户就无法正常加载其资源了。

在你的 urls.py 中添加以下内容,确保 jsi18n 在你的原 admin site 之前
``` python
def i18n_javascript(request):
    return admin.site.i18n_javascript(request)
patterns = [
    ...
    url(r'^admin/jsi18n', i18n_javascript),
    url(r'^admin/', include(admin.site.urls))
]
```
 如果没有上面的设置，普通用户无法访问admin的jsi18n
 
django admin site 专门使用一套 jQuery 为了不会和其它 jQuery 干扰，使用方式与一般$开头不同，是django.jQuery。
如果页面本身就已经引入了 jQuery，那么只需要在 jquery.init.js 上修改一下即可，否则请直接引入 admin site 的 jQuery 库。
``` javascript
<script src="{% static 'admin/js/jquery.js' %}"></script>
<script src="{% static 'admin/js/jquery.init.js' %}"></script>
```

jquery.init.both.js
``` javascript
var django = {
    "jQuery": jQuery.noConflict(true)
};
var jQuery = django.jQuery;
var $=jQuery;
```

目前Jquery.init.js里是下面这个，能正常工作，但是会报错django没找到
``` javascript
var django = django || {};
django.jQuery = jQuery.noConflict(true);
```
最后一项window.\_\_admin_media_prefix\_\_如果不能正确设定，控件的图标将无法显示。设置是在admin/base.html中找到的，在DateTimeShortcuts.js中有描述

> Get admin_media_prefix by grabbing it off the window object. It’s set in the admin/base.html template, so if it’s not there, someone’s overridden the template. In that case, we’ll set a clearly-invalid value in the hopes that someone will examine HTTP requests and see it.

最后，使用时需要注意的是，这个控件使用的是字符型输入框，最后上传的日期格式为2016/10/26，而后端处理时的标准日期格式为2016-10-26，所以最后后端接收到数据后还需转换一下。

如果在form中定义，首先引入widget，并覆盖原来的日期表单
``` python
from django.contrib.admin import widgets

class DailyInspectionForm(forms.ModelForm):

    date = forms.DateTimeField(widget=widgets.AdminDateWidget(), label=u'时间')
    
    def __init__(self, *args, **kwargs):
        super(DailyInspectionForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].widget = widgets.AdminDateWidget()
```

## 用media简化实现
下面js是需要再html里面引入的

``` javascript
<script src="/admin/jsi18n/"></script>
<script src="{% static 'admin/js/core.js' %}"></script>
<script src="{% static 'admin/js/jquery.init.js' %}"></script>
<script src="{% static 'admin/js/calendar.js' %}"></script>
<script src="{% static 'admin/js/admin/DateTimeShortcuts.js' %}"></script>
<script type="text/javascript">window.__admin_media_prefix__ = "{% filter escapejs %}{% static 'admin/' %}{% endfilter %}";</script>
```
查看代码,```calendar.js```和```DateTimeShortcuts.js```已经在AdminDateWidget的media里包括了

``` python
class AdminDateWidget(forms.DateInput):
    @property
    def media(self):
        js = ["calendar.js", "admin/DateTimeShortcuts.js"]
        return forms.Media(js=[static("admin/js/%s" % path) for path in js])
```

给form添加media

``` python
class DailyInspectionForm(forms.ModelForm):
    class Media:
        css = {
            'form': ('css/form_horizontal_layout.css',)
        }
        js = ['js/form_horizontal_layout.js']


    #inherit from BaseForm
    @property
    def media(self):
        """
        Provide a description of all media required to render the widgets on this form
        """        
        media = Media(js=[static('js/jquery.init.both.js'), '/admin/jsi18n/', static('admin/js/core.js')])
        for field in self.fields.values():
            for item in field.widget.media._js:
                if not item.split('/')[-1] in ''.join(media._js):
                    media = media + Media(js=[item])

        media = media + Media(self.Media)

        return media
```

模板引用如下
``` html
{{form.media.js}}
<script type="text/javascript">window.__admin_media_prefix__ = "{% filter escapejs %}{% static 'admin/' %}{% endfilter %}";</script> 
```

```admin_media_prefix```这个变量在DateTimeShortcuts.js里面会用到

参考
- [在 Django admin site 之外使用其日历控件](http://blog.xavierskip.com/2016-10-22-django-admit-calendar-widget/)
- [将django 管理端的时间控件用于前端](https://www.douban.com/note/350934079/)
- https://stackoverflow.com/questions/38601/using-django-time-date-widgets-in-custom-form
- https://docs.djangoproject.com/en/1.8/topics/forms/media/#assets-as-a-static-definition

