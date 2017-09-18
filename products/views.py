#encoding=utf-8
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ProductCreateForm, ProductImageForm
from .models import Category, ProductImage
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from django_filters import FilterSet, CharFilter, NumberFilter
# Create your views here.
from .forms import VariationInventoryFormSet, ProductFilterForm
from .mixins import StaffRequiredMixin

from .models import Product, Variation, Category
from django.utils.translation import gettext_lazy as _

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "products/product_list.html"


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        product_set = obj.product_set.all()
        default_products = obj.default_category.all()
        products = ( product_set | default_products ).distinct()
        context["products"] = products
        context["categories"] = Category.objects.all()
        return context



class VariationListView(StaffRequiredMixin, ListView):
    model = Variation
    queryset = Variation.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VariationListView, self).get_context_data(*args, **kwargs)
        context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset()) 
        return context

    def get_queryset(self, *args, **kwargs):
        product_pk = self.kwargs.get("pk")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            queryset = Variation.objects.filter(product=product) 
        return queryset

    def post(self, request, *args, **kwargs):
        formset = VariationInventoryFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                new_item = form.save(commit=False)
                #if new_item.title:
                product_pk = self.kwargs.get("pk")
                product = get_object_or_404(Product, pk=product_pk)
                new_item.product = product
                new_item.save()
                
            messages.success(request, "Your inventory and pricing has been updated.") 
            return redirect("products")
        raise Http404

class ProductFilter(FilterSet):
    title = CharFilter(name='title', lookup_type='icontains', distinct=True)
    category = CharFilter(name='categories__title', lookup_type='icontains', distinct=True)
    category_id = CharFilter(name='categories__id', lookup_type='icontains', distinct=True)
    min_price = NumberFilter(name='variation__price', lookup_type='gte', distinct=True) # (some_price__gte=somequery)
    max_price = NumberFilter(name='variation__price', lookup_type='lte', distinct=True)
    class Meta:
        model = Product
        fields = [
            'min_price',
            'max_price',
            'category',
            'title',
            'description',
        ]


def product_list(request):
    qs = Product.objects.all()
    ordering = request.GET.get("ordering")
    if ordering:
        qs = Product.objects.all().order_by(ordering)
    f = ProductFilter(request.GET, queryset=qs)
    return render(request, "products/product_list.html", {"object_list": f })


class FilterMixin(object):
    filter_class = None
    search_ordering_param = "ordering"

    def get_queryset(self, *args, **kwargs):
        try:
            qs = super(FilterMixin, self).get_queryset(*args, **kwargs)
            return qs
        except:
            raise ImproperlyConfigured("You must have a queryset in order to use the FilterMixin")

    def get_context_data(self, *args, **kwargs):
        context = super(FilterMixin, self).get_context_data(*args, **kwargs)
        qs = self.get_queryset()
        ordering = self.request.GET.get(self.search_ordering_param)
        if ordering:
            qs = qs.order_by(ordering)
        filter_class = self.filter_class
        if filter_class:
            f = filter_class(self.request.GET, queryset=qs)
            context["object_list"] = f
        return context

class ProductListView(FilterMixin, ListView):
    model = Product
    queryset = Product.objects.all()
    filter_class = ProductFilter

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q") #None
        context["filter_form"] = ProductFilterForm(data=self.request.GET or None)        
        context["categories"] = Category.objects.all()        
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
                )
            try:
                qs2 = self.model.objects.filter(
                    Q(price=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs

    def dispatch(self, request, *args, **kwargs):
        ''' need config i18n before use this
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("product"),request.path_info),
        ])
        '''

        request.breadcrumbs([
            ("Home",reverse("home", kwargs={})),
            ("product",request.path_info),
        ])
        return super(ProductListView, self).dispatch(request,args,kwargs)

import random
class ProductDetailView(DetailView):
    model = Product
    #template_name = "product.html"
    #template_name = "<appname>/<modelname>_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        #context["related"] = Product.objects.get_related(instance).order_by("?")[:6]
        context["related"] = sorted(Product.objects.get_related(instance)[:6], key= lambda x: random.random())
        context["images"] = ProductImage.objects.filter(product=instance)[1:]
        return context

    def dispatch(self, request, *args, **kwargs):
        ''' need config i18n before use this
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("product"),request.path_info),
        ])
        '''

        instance = self.get_object()
        request.breadcrumbs([
            ("Home",reverse("home", kwargs={})),
            ("product",reverse("products", kwargs={})),
            (instance.title,request.path_info),
        ])
        return super(ProductDetailView, self).dispatch(request,args,kwargs)


def product_detail_view_func(request, id):
    #print "coming"
    #product_instance = Product.objects.get(id=id)
    product_instance = get_object_or_404(Product, id=id)
    try:
        product_instance = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    except:
        raise Http404

    template = "products/product_detail.html"
    context = {    
        "object": product_instance
    }

    return render(request, template, context)


from PIL import Image 
from django.conf import settings
import os
def upload_to(filename, title, id):
    if filename:
        img=Image.open(filename)
        slug = slugify(title)
        basename, file_extension = filename.name.split(".")
        new_filename = "%s-%s.%s" %(slug, id, file_extension)        
        photoname = os.path.join("products", slug, new_filename)
        if settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ: 
            pass
        else:
            photopath = os.path.join(settings.MEDIA_ROOT, "products", slug)
            if not os.path.exists(photopath):
                os.makedirs(photopath)
        return photoname
    
class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductCreateForm
    success_url = "/products"


    def get_context_data(self, *args, **kwargs):
        context = super(ProductCreateView, self).get_context_data(*args, **kwargs)
        context["image_form"] = ProductImageForm()
        return context

    def get_form(self, *args, **kwargs):
        form = super(ProductCreateView, self).get_form(*args, **kwargs)

        form.fields['categories'].queryset  = Category.objects.all()
        form.fields['default'].queryset  = Category.objects.all()

        return form

    
    def post(self, request, *args, **kwargs):
        postresult = super(ProductCreateView, self).post(request, *args, **kwargs)

        if 1:
            in_mem_image_file=request.FILES['image']     
            if in_mem_image_file:
                photoname = upload_to(in_mem_image_file, self.object.title, self.object.id)

                if settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ: 
                    from sae import storage
                    #from sae.storage import Bucket
                    #bucket = Bucket('media')
                    from saewrapper.storage.bucket import SAEBucket
                    SAEBucket().put_object(photoname,in_mem_image_file.file.getvalue())
                    #object_content = bucket.get_object_contents(photoname) 
                else:
                    img=Image.open(in_mem_image_file)
                    img.save(os.path.join(settings.MEDIA_ROOT, photoname))
                
                ProductImage.objects.create(product = self.object, 
                        image = photoname)

        # BELOW ALSO WORKS
        else:
            imageForm = ProductImageForm(request.POST, request.FILES)
            if imageForm.is_valid():
                productImage = imageForm.save(commit=False) 
                productImage.product = self.object
                productImage.save()
                return postresult

        return postresult