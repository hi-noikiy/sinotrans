
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
