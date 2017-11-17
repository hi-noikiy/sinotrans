
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .forms import SignUpForm,ContactForm
from .models import Banner, Article
from django.utils.translation import ugettext as _


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse
# from django.contrib.auth.forms import AuthenticationForm
# from django.utils.http import is_safe_url
# from django.http import HttpResponseRedirect

from inspection.models import DailyInspection, shelf_inspection


def home(request):    

    title = 'Sign Up now'
    banners = Banner.objects.filter(active=True).order_by("?")[:6]

    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
        'banners':banners,

    }

    try:
        context["categories"] = Article.article_category
        context["objects"] = [(category[0], Article.objects.filter(category=category[0])) for category in Article.article_category]
    except:
        pass

    try:
        context["dailyinspection_object_list"] = DailyInspection.objects.all()[:8]
    except:
        pass

    try:
        records_list = [(object, \
            object.shelf_inspection_record_set.filter(use_condition=1).count(), \
            object.shelf_inspection_record_set.filter(is_locked=False).count(), \
            object.shelf_inspection_record_set.filter(gradient__gt=1.4).count()) for object in shelf_inspection.objects.all()]
        context["shelf_inspection_records"] = records_list[:10]
    except:
        pass
    
    if form.is_valid():
        #form.save()
        #print request.POST['email'] #not recommended, raw data without validation
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name:
        #     instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)


def contact(request):
    title = 'Contact Us'    
    title_align_center = True
    form = ContactForm(request.POST or None)

    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        #     #print form.cleaned_data.get(key)

        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print email, message, full_name
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, form_email]

        contact_message = "%s: %s via %s"%( 
                form_full_name, 
                form_message, 
                form_email)
        some_html_message = """
        <h1>hello</h1>
        """

        # import smtplib
        # try:
        #     smtpObj = smtplib.SMTP() 
        #     smtpObj.connect(settings.EMAIL_HOST, 25)
        #     smtpObj.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)  
        #     smtpObj.sendmail(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER, some_html_message)
        #     print "sent successfully !!!!!!!!!!!!!!!!"
        # except smtplib.SMTPException:
        #     print "Error: sent fail $$$$$$$$$$$$$$"

        send_mail(subject, 
                contact_message, 
                from_email, 
                to_email, 
                html_message=some_html_message,
                fail_silently=False)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "forms.html", context)

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/article_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["object"] = self.get_object()
        return context        

    def get(self, request, *args, **kwargs):
        return super(ArticleDetailView, self).get(request, *args, **kwargs) 

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Newsletter"),reverse("article_list", kwargs={})),
            (instance.title,request.path_info),
        ])
        return super(ArticleDetailView, self).dispatch(request,args,kwargs)      

class ArticleListView(ListView): 
    model = Article
    template_name = "article/article_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        #context["category"] = list(set([article.category for article in Article.objects.all()]))
        context["categories"] = Article.article_category
        context["objects"] = [(category[0], Article.objects.filter(category=category[0])) for category in Article.article_category]
        return context       

    def dispatch(self, request, *args, **kwargs):
        request.breadcrumbs([
            (_("Home"),reverse("home", kwargs={})),
            (_("Newsletter"),reverse("article_list", kwargs={})),
        ])
        return super(ArticleListView, self).dispatch(request,args,kwargs)   



