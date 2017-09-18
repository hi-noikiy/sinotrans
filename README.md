"# zakkabag" 
[Init 2016/2/16](https://github.com/navicester/zakkabag/commit/142d9cdac158b55f8e168c261cc9048949255f9b)

# 轮播图
http://getbootstrap.com/javascript/#carousel

# 图片上传

在表单中加入`enctype="multipart/form-data；`如果不加`enctype="multipart/form-data：`得不到图片信息，只有路径

FILES是个字典，它包含每个FileField的键 （或者ImageField，FileField的子类）。这样的话就可以用request.FILES['File']来存放表单中的这些数据了。 
注意request.FILES只有在请求方法为POST，并且发送请求的`<form>`拥有`enctype="multipart/form-data`属性时，才会包含数据。否则request.FILES为空

定义图片form

products/forms.py
``` python
class ProductImageForm(forms.ModelForm):
	class Meta:
		model = ProductImage
		fields = [
			'image',
		]
```

在模板里添加form

products/templates/products/product_create.html
``` python
-<form method='POST' action=''>{% csrf_token %}
+<form method='POST' enctype="multipart/form-data" action=''>{% csrf_token %}
 {{ form|crispy }}
+{{image_form.as_p}}
 <input class = 'btn btn-primary' type='submit' value='Submit' />
 </form>
```

创建formview

products/views.py
``` python
class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductCreateForm
success_url = "/products"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductCreateView, self).get_context_data(*args, **kwargs)
        context["image_form"] = ProductImageForm()
        return context

    def post(self, request, *args, **kwargs):
        postresult = super(ProductCreateView, self).post(request, *args, **kwargs)

        if 0: #方法1
            filename=request.FILES['image']
            from PIL import Image 
            if filename:
                img=Image.open(filename)
                title = self.object.title
                slug = slugify(title)
                basename, file_extension = filename.name.split(".")
                new_filename = "%s-%s.%s" %(slug, self.object.id, file_extension)
                from django.conf import settings
                import os
                photoname = os.path.join("products", slug, new_filename)
                photopath = os.path.join(settings.MEDIA_ROOT, "products", slug)
                if not os.path.exists(photopath):
                    os.makedirs(photopath)
                img.save(os.path.join(settings.MEDIA_ROOT, photoname))
                ProductImage.objects.create(product = self.object, 
                    image = photoname)

        # BELOW ALSO WORKS 方法2
        else:
            imageForm = ProductImageForm(request.POST, request.FILES)
            if imageForm.is_valid():
                productImage = imageForm.save(commit=False) 
                productImage.product = self.object
                productImage.save()
                return postresult

        return postresult    
```
img=Image.open(filename)

img.save(os.path.join(settings.MEDIA_ROOT, photoname))

imageForm = ProductImageForm(request.POST, request.FILES)

productImage = imageForm.save(commit=False) 

https://docs.djangoproject.com/en/1.2/topics/http/file-uploads/

## 参考文档
- [django上传图片](http://www.cnblogs.com/RoundGirl/p/5395658.html)
- [Django and AJAX image uploads https://github.com/pcraciunoiu/kitsune/](https://blog.mozilla.org/webdev/2010/09/17/django-and-ajax-image-uploads/)
- [jQuery File Upload Demo](https://blueimp.github.io/jQuery-File-Upload/)

- [python image模块](http://www.cnblogs.com/DjangoBlog/p/3557744.html)
- [Python创建目录文件夹](http://www.qttc.net/201209207.html)
- [豆瓣浅论Django文件上传](https://www.douban.com/group/topic/21131470/)
- [Django Ajax 文件上传及进度显示](http://onlypython.group.iteye.com/group/wiki/1517-django-ajax-file-uploads-and-progress-display)
- [Ajax 和 jQuery 实现进度条＋上传文件到Django](http://blog.csdn.net/dimply/article/details/42425373)
- [ajax异步上传图片 ajax 异步上传带进度条视频并提取缩略图](http://www.alonely.com.cn/Ajax/20161025/58632.html)
- [Django image upload](http://cloudinary.com/documentation/django_image_upload)





