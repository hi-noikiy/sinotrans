from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse
from .models import Crowdfunding
from .forms import CrowdfundingCreateForm
from .mixins import StaffRequiredMixin
import json

# Create your views here.
class CrowdfundingListView(ListView, StaffRequiredMixin):
    model = Crowdfunding
    queryset = Crowdfunding.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(CrowdfundingListView, self).get_context_data(*args, **kwargs)
        # context["now"] = timezone.now()     
        return context

    def get_queryset(self, *args, **kwargs):
        return  super(CrowdfundingListView, self).get_queryset(*args, **kwargs)

class CrowdfundingDetailView(DetailView):
    model = Crowdfunding
    def get_context_data(self, *args, **kwargs):
        context = super(CrowdfundingDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        from wechat.client import WechatAPI
        api = WechatAPI(request = self.request)
        context["signPackage"] = api.getSignPackage()
        return context        

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.is_ajax():
            if "addFavorite" == request.GET.get("purpose", 'addFavorite'):                
                if True == obj.is_favorite:
                    obj.is_favorite = False
                else:
                    obj.is_favorite = True
                obj.save()
                data = {       
                        "is_favorite": obj.is_favorite,                          
                        }

                return JsonResponse(data) 
        else:
            return super(CrowdfundingDetailView, self).get(request, *args, **kwargs) 

class CrowdfundingCreateView(CreateView):
    template_name = 'crowdfundings/crowdfunding_create.html'
    form_class = CrowdfundingCreateForm
    success_url = "/crowdfunding"

    def get_context_data(self, *args, **kwargs):
        context = super(CrowdfundingCreateView, self).get_context_data(*args, **kwargs)
        context["user_id"] = self.request.user.id
        return context

    def get_form(self, *args, **kwargs):
        form = super(CrowdfundingCreateView, self).get_form(*args, **kwargs)

        # form.fields['categories'].queryset  = Category.objects.all()
        # form.fields['default'].queryset  = Category.objects.all()

        return form

    # def get_success_url(self):
    #     return reverse("CrowdfundingListView")

    def post(self, request, *args, **kwargs):
        # postresult = super(CrowdfundingCreateView,self).post(request, args, kwargs)
        if request.is_ajax():
            id = request.POST['id']
            f = request.FILES['picture']
            path = '/var/www/pictures/%s' % id
            destination = open(path, 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        else:
            crowdfundingForm = CrowdfundingCreateForm(request.POST, request.FILES)
            if crowdfundingForm.is_valid():
                crowdfunding = crowdfundingForm.save(commit=False)
                crowdfunding.user = request.user
                crowdfunding.save()
                # return self.form_valid(crowdfundingForm)
                #return HttpResponseRedirect(reverse("CrowdfundingListView"))
                return HttpResponseRedirect(crowdfunding.get_absolute_url())
            else:
                return postresult
                #return self.form_invalid(crowdfundingForm)

            # if 0:
            #     filename=request.FILES['image']
            #     from PIL import Image 
            #     if filename:
            #         img=Image.open(filename)
            #         title = self.object.title
            #         slug = slugify(title)
            #         basename, file_extension = filename.name.split(".")
            #         new_filename = "%s-%s.%s" %(slug, self.object.id, file_extension)
            #         from django.conf import settings
            #         import os
            #         photoname = os.path.join("products", slug, new_filename)
            #         photopath = os.path.join(settings.MEDIA_ROOT, "products", slug)
            #         if not os.path.exists(photopath):
            #             os.makedirs(photopath)
            #         img.save(os.path.join(settings.MEDIA_ROOT, photoname))
            #         ProductImage.objects.create(product = self.object, 
            #             image = photoname)

            # # BELOW ALSO WORKS
            # else:
            #     imageForm = ProductImageForm(request.POST, request.FILES)
            #     if imageForm.is_valid():
            #         productImage = imageForm.save(commit=False) 
            #         productImage.product = self.object
            #         productImage.save()
            #         return postresult

            return postresult              

# from django.db.models.signals import pre_save

# def crowdfunding_pre_save_receiver(sender, instance, *args, **kwargs):
#    qty = instance.quantity
#    if qty >= 1:
#        price = instance.item.get_price()
#        line_item_total = Decimal(qty) * Decimal(price)
#        instance.line_item_total = line_item_total

# pre_save.connect(crowdfunding_pre_save_receiver, sender=Crowdfunding)


def CommentsShow(request, pk=''):
    crowdfunding = Crowdfunding.objects.get(id=pk)
    context={
        'object': crowdfunding,
    }

    #return render_to_response('comments/comments_tree.html', {"object": crowdfunding})
    return render(request, "crowdfundings/comments_render.html", context)
    #return render(request, "comments/comments_tree.html", context)
    
