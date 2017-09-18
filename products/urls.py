from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView

from .views import ProductDetailView, ProductListView, ProductCreateView, VariationListView

urlpatterns = [
    # Examples:

    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^create$', ProductCreateView.as_view(), name='products_create'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),   
    url(r'^exchangerule$',
        TemplateView.as_view(template_name='products/exchange_rule.html'),
        name='exchange_rule'),     
]