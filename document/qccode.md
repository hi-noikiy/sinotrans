# 安装
python qrcode需要用到PIL和qrcode库，首先安装这些库

```
pip install qrcode
pip install image
```

pypi： https://pypi.python.org/pypi/qrcode

# 二维码生成
## 简单用法
``` python
import qrcode
img = qrcode.make('some data here')
img.save('somedatahere.jpg')
img.show()
```

## 高级用法
``` python
import qrcode
qr=qrcode.QRCode(
     version = 2,
     error_correction = qrcode.constants.ERROR_CORRECT_L,
     box_size=10,
     border=10,)
qr.add_data('http://zakkabag.applinzi.com/newsletter/')
qr.make(fit=True)
img = qr.make_image()
img.show()
#img.save('test.jpg')
```
**参数解释**
> The **version** parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). 
> Set to None and use the **fit** parameter when making the code to determine this automatically.
>
> The **error_correction** parameter controls the error correction used for the QR Code. The following four constants are made available on the qrcode package:
>
> ERROR_CORRECT_L  
> About 7% or less errors can be corrected.  
> ERROR_CORRECT_M (default)  
> About 15% or less errors can be corrected.  
> ERROR_CORRECT_Q  
> About 25% or less errors can be corrected.  
> ERROR_CORRECT_H.  
> About 30% or less errors can be corrected.
>
> The **box_size** parameter controls how many pixels each “box” of the QR code is.
>
> The **border** parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).

## 生成带图案的二维码
生成带图案的二维码会把icon合并要二维码图片中，下面函数能实现该功能
``` python
'''
icon size is 1/4
'''
def gen_imge(img, factor = 4, icon = "logo.png"):
    img = img.convert("RGBA")
    icon = Image.open(icon)

    img_w,img_h = img.size    
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w,icon_h = icon.size
    if icon_w >size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)

    w = int((img_w - icon_w)/2)
    h = int((img_h - icon_h)/2)
    icon = icon.convert("RGBA")
    img.paste(icon,(w,h),icon)
	
    return img
```
在前面img生成之后，调用还函数叠加logo

``` python
import qrcode
from PIL import Image

qr=qrcode.QRCode(
     version = 2,
     error_correction = qrcode.constants.ERROR_CORRECT_H,
     box_size=10,
     border=10,)
qr.add_data('http://zakkabag.applinzi.com/newsletter/')
qr.make(fit=True)
img = qr.make_image()

#add icon to qrcode image
img = gen_imge(img)

img.show()
```
插入的log

![Alt text](img/logo.png)

生成的图片

![Alt text](img/qr_with_logo.png)

注意：这种方法是直接用一个图片叠加在生成的二维码图片上，会导致原二维码信息丢失，难以识别。需要将容错参数改为 ERROR_CORRECT_H

# 二维码解析
- [qr-code-decoder-library-for-python](https://stackoverflow.com/questions/9310280/qr-code-decoder-library-for-python)
- [How to decode a QR-code image in (preferably pure) Python?](http://www.howtobuildsoftware.com/index.php/how-do/bIAP/python-decode-qr-code-zxing-zbar-how-to-decode-a-qr-code-image-in-preferably-pure-python)
- [how-to-decode-a-qr-code-image-in-preferably-pure-python](https://stackoverflow.com/questions/27233351/how-to-decode-a-qr-code-image-in-preferably-pure-python)
- [decoding-qr-code-in-python](https://stackoverflow.com/questions/33519479/decoding-qr-code-in-python)
- [qr-code-decoder-library-for-python](https://stackoverflow.com/questions/9310280/qr-code-decoder-library-for-python)
- https://pypi.python.org/pypi/zbar
- https://pypi.python.org/pypi/qrtools/
- https://github.com/primetang/qrtools
- https://launchpad.net/qr-tools
- https://pypi.python.org/pypi/qrcode
- [Python如何识别二维码](https://zhuanlan.zhihu.com/p/21292914)
- [Python zxing 库解析（条形码二维码识别）](http://www.cnblogs.com/oucsheep/p/6269813.html)






