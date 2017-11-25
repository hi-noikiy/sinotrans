from django.conf import settings
from django.conf.urls.static import static
from inspection.admin import my_admin_site
if settings.USE_EXPLICIT_LANG_URL:
    from django.conf.urls.i18n import i18n_patterns as url_patterns
else:
    from django.conf.urls import patterns as url_patterns
from django.conf.urls import patterns, include, url

from django.contrib import admin

from newsletter.views import home, contact
from zakkabag.views import about, sitemap, set_language
# from .views import CKEditorImageUpload
					
admin.autodiscover()

def i18n_javascript(request):
    return admin.site.i18n_javascript(request)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),   
    url(r'^about/$', about, name='about'),    
    url(r'^about/sitemap$', sitemap, name='sitemap'),

    url(r'^admin/jsi18n', i18n_javascript),  # added for AdminDateTimeWidget
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sino/', include(my_admin_site.urls)),
#    url(r'^sino/', my_admin_site.urls, namespace='sino'),
	

    url(r'^personalcenter/', include('personalcenter.urls')),
    # url(r'^crowdfundings/', include('crowdfundings.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^auth/', include('authwrapper.urls')),
    url(r'^inspection/', include('inspection.urls')),
    url(r'^fileupload/', include('fileuploadwrapper.urls')),
    url(r'^equipments/', include('equipments.urls')),
    url(r'^outsourcing/', include('outsourcing.urls')),
    url(r'^trainings/', include('trainings.urls')),
    url(r'^picking/', include('picking.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),    
    url(r'^setlang/$', set_language, name='setlang'),
    url(r'^phone_login/', include('phone_login.urls')),

    # url(r'^upload/ckeditorimage/$', CKEditorImageUpload, name='ckeditor_image_upload'), 
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
]

urlpatterns +=  [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

import os
if settings.DEBUG:
    if settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ:
        pass
    else:
    	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
