
# 安装
> pip install django-ckeditor

# settings.py 配置

## 添加到INSTALLED_APPS

``` python
INSTALLED_APPS = [ 
    'ckeditor',
]
```


## 设置语言

CKEDITOR_CONFIGS = {
    'default': {
        #'toolbar': 'Full',
        #'height': 300,
        #'width': 300,
        'language': 'zh-cn',  # ckeditor is not align with django latest lan (>1.9)  I also tried config.js, it doesn't work # see widgets.py for the language settings
    },
}

我的版本已经5.2.2，但是依然里面支持的语言是zh-cn，而在django 1.9之后，已经用zh-hans代替了，所以只能添加上面的配置加语言奢侈老的

# 使用
``` python
class Article(models.Model):
    content = RichTextField('content')
```    

# 文件上传

## INSTALLED_APPS
如果要添加图片上传功能，INSTALLED_APPS同时添加ckeditor_uploader

``` python
INSTALLED_APPS = [ 
    'ckeditor',
    'ckeditor_uploader',
]
```

## 设置上传路径

CKEDITOR_UPLOAD_PATH = 'ckeditor/uploads'

它是相对路径，在MEDIA_URL下面

## url映射
在项目的urls.py中添加CKEditor的URL映射
``` python
url(r'^ckeditor/', include('ckeditor_uploader.urls')),
```
## JS修改
1. 找到image.js这个文件，搜索“upload”可以找到这一段id:'Upload',hidden:true。  

实际上上传功能被隐藏了，把上面的true改成false，再打开编辑器，就能找到上传功能了。

有的显示hidden:!0

“预览”中有一坨鸟语，看得很不爽，首先要去掉这些。在ckeditor/config.js中加上一个配置项：
config.image_previewText = ' ';

2. 在ckeditor/config.js中配置。加入：```config.filebrowserUploadUrl = "/ckeditor/upload/";```这个是post图片的URL

ckeditor_uploader.view.ImageUploadView会处理这个post请求，如果想自己添加裁剪等功能，可以改写这个函数或者通过修改path重写这个处理函数

3. 如果启用了csrf，会报错。因为ckeditor不会自带csrf，所以要自己添加。

打开ckeditor.js源文件，插入函数：

``` javascript
function getCookie(name){   
    var strCookie=document.cookie;   
    var arrCookie=strCookie.split("; ");   
    for(var i=0;i<arrCookie.length;i++){   
        var arr=arrCookie[i].split("=");   
        if(arr[0]==name)return arr[1];   
    }   
    return "";   
}   
```

然后搜索：multipart/form-data，会找到一个form，在这个form里面插入：
``` html
<input type="hidden" name="csrfmiddlewaretoken" value="'+getCookie("csrftoken")+'">  
```

但是ckeditor.js做了html的encode处理，用下面语句代替
``` html
\x3cinput type\x3d"hidden" name\x3d"csrfmiddlewaretoken" value\x3d"'+getCookie("csrftoken")+'"\x3e```


# 参考文档
- [django教你熟练掌握富文本编辑器CKEditor的方法](http://www.php.cn/python-tutorials-360824.html)
- [django下ckeditor上传图片的实现](http://blog.csdn.net/ypq5566/article/details/37594371)
- [CKEditor图片上传实现详细步骤(使用Struts 2)](http://blog.csdn.net/xiao__gui/article/details/7684505)

