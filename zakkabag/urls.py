from django.conf import settings
from django.conf.urls.static import static
if settings.USE_EXPLICIT_LANG_URL:
    from django.conf.urls.i18n import i18n_patterns as url_patterns
else:    
    from django.conf.urls import patterns as url_patterns
from django.conf.urls import patterns, include, url

from django.contrib import admin

from carts.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView
from orders.views import (
                    AddressSelectFormView, 
                    UserAddressCreateView, 
                    OrderList, 
                    OrderDetail)
					
admin.autodiscover()

def i18n_javascript(request):
    return admin.site.i18n_javascript(request)


urlpatterns = url_patterns('',
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^home$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),   
    url(r'^about/$', 'zakkabag.views.about', name='about'),    
    url(r'^about/sitemap$', 'zakkabag.views.sitemap', name='sitemap'),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/jsi18n', i18n_javascript),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.urls_categories')),

    url(r'^orders/$', OrderList.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),

    url(r'^cart/$', CartView.as_view(), name='cart'), 
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),  

    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),    
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='order_address'),   
    url(r'^checkout/address/add/$', UserAddressCreateView.as_view(), name='user_address_create'), 
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'),   	

    url(r'^personalcenter/', include('personalcenter.urls')),
    url(r'^crowdfundings/', include('crowdfundings.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^auth/', include('authwrapper.urls')),
    url(r'^inspection/', include('inspection.urls')),
    url(r'^wechat/', include('wechat.urls')),
    url(r'^fileupload/', include('fileuploadwrapper.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),    

    url(r'^phone_login/', include('phone_login.urls')),    

    #url(r'^setlang/$', 'django.views.i18n.set_language', name = 'setlang'),
    url(r'^setlang/$', 'zakkabag.views.set_language', name='setlang'),

    #url(r'^ckeditor/', include('ckeditor.urls')),
    
    # url(r'^articles/comments/', include('django_comments.urls')),   
)

urlpatterns += patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
)


'''
urlpatterns += patterns('',
    url(r'^zakkabag/',include('zakkabag.urls')),
)
'''

import os
if settings.DEBUG:
    if settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ:
        pass
    else:
    	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)