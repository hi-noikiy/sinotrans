from django.db import models
 
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import post_delete, post_save, pre_save
from .utils import file_cleanup, file_cleanup2, save_raw_instance
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.http import Http404
from django.utils import timezone
from datetime import datetime, timedelta
from fields import ThumbnailImageField
from django.conf import settings
from uuslug import slugify as uuslugify

# Create your models here.
class InspectionMixin(models.Model):
    equipment_use_condition = [
        ('normal', _('Normal')),
        ('breakdown', _('Breakdown')),
    ]

    check_person = models.CharField(_('Check Person'), max_length=30, blank=True) 
    owner = models.CharField(_('Owner'), max_length=30, blank=True, null=True)
    forecast_complete_time = models.DateField(_('Forecast Complete Time'), auto_now_add=False, auto_now=False, null=True, blank=True)
    completed_time = models.DateTimeField(_('rectification completed time'), auto_now_add=False, auto_now=False, null=True, blank=True)    
    check_result = models.CharField(_('Check Result'), choices=equipment_use_condition, max_length=30, blank=True) 
    check_date = models.DateField(_('Check Date'),auto_now_add=True, auto_now=False)

    class Meta:
        abstract=True


RESULT_OPTION = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

# inspection/office/
def image_upload_to(instance, filename):
    title, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(instance.timestamp, slugify(title), file_extension)
    return "inspection/%s/%s" %(instance.location, new_filename)

class OfficeInspection(models.Model):
    plug = models.CharField(_('plug'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    power = models.CharField(_('power'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    comments = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to=image_upload_to, blank=True, null=True)

    def __unicode__(self): 
        return "Office " + self.location

    def get_absolute_url(self):
        return reverse("OfficeInspection_detail", kwargs={"pk": self.id })



def image_upload_to_dailyinspection(instance, filename):
    print filename
    title, file_extension = filename.split(".")
    #new_filename = "%s-%s.%s" %(instance.created.strftime('%Y-%m-%d-%H-%M-%S'), slugify(title), file_extension)
    if settings.UUSLUGIFY == True:
        new_filename = "%s-%s.%s" %(timezone.now().strftime('%Y%m%d%H%M%S'), uuslugify(title), file_extension)
    else:
        new_filename = "%s-%s.%s" %(timezone.now().strftime('%Y%m%d%H%M%S'), title, file_extension) # created was not ready for CreateView
    return "dailyinspection/%s/%s" %(instance.category, new_filename)

class DailyInspectionManager(models.Manager):
    def external(self, *args, **kwargs):
        return super(DailyInspectionManager,self).filter(rectification_status__iexact='completed')

    def overdue(self, *args, **kwargs):
        return super(DailyInspectionManager,self).filter(rectification_status__icontains='uncompleted').filter(due_date__lte=timezone.now().date())


class DailyInspection(models.Model):

    daily_insepction_category = (
        ('people', _('People')),
        ('device', _('Device')),
        ('machine', _('Machine')),
        ('method', _('Method')),
        ('environment', _('Environment')),
    )

    # index can only be 1 char, see SelectMultiple:render & Select(Widget):render_options / selected_choices = set(force_text(v) for v in selected_choices) ==> bug ? set([force_text(v)]
    daily_insepction_impact = (
        ('1', _('economic loss')),
        ('2', _('personnel injury')),
        # ('3', _('non-conformance 5SS standard')),
    )

    daily_insepction_correction_status = (
        ('completed', _('Completed')),
        ('uncompleted', _('Uncompleted')),
    )

    daily_insepction_warehouse = (
        ('3', '3#'),
        ('5', '5#'),
    )

    daily_insepction_location = (
        ('1', _('Storage Area')),
    )
 
    category = models.CharField(_('Category'), max_length=30, choices = daily_insepction_category, blank=False, default = 'device')
    inspection_content = models.CharField(_('Inspection Content'), max_length=30, blank=False)
    impact = models.CharField(_('Impact'), max_length=30, blank=False)
    rectification_measures = models.TextField(_('Rectification Measures'), max_length=500, blank=False)
    rectification_status = models.CharField(_('Rectification Status'), max_length=30, choices = daily_insepction_correction_status, blank=False, default = 'uncompleted')
    owner = models.CharField(_('Owner'), max_length=30, blank=False)
    inspector = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_('Inspector'), null=True, blank=True) 
    due_date = models.DateField(_('Due Date'), auto_now_add=False, auto_now=False)
    created = models.DateTimeField(_('Inspection Created Date'), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(_('Inspection Updated Date'), auto_now_add=False, auto_now=True)
    completed_time = models.DateTimeField(_('rectification completed time'), auto_now_add=False, auto_now=False, null=True, blank=True)
    image_before = ThumbnailImageField(verbose_name = _('Picture before Rectification'), upload_to=image_upload_to_dailyinspection, blank=False, null=True)
    image_after = models.ImageField(_('Picture after Rectification'), upload_to=image_upload_to_dailyinspection, blank=True, null=True)
    #warehouse = models.CharField(_('Warehouse'), max_length=30, choices = daily_insepction_warehouse, blank=False, default = '3#')
    location = models.CharField(_('Location'), max_length=30, choices = daily_insepction_location, blank=False, default = '1')

    objects = DailyInspectionManager()
    
    def __unicode__(self): 
        return _("Daily Inspection") +"-" +  self.inspection_content

    def get_absolute_url(self):
        return reverse("dailyinspection_detail", kwargs={"pk": self.id })    

    def get_absolute_url_update(self):
        return reverse("dailyinspection_update", kwargs={"pk": self.id })    

    def get_absolute_url_delete(self):
        return reverse("dailyinspection_delete", kwargs={"pk": self.id })    


    def get_image_url_before(self):
        img = self.image_before
        if img:
            return img.url
        return img     

    def get_image_url_after(self):
        img = self.image_after
        if img:
            return img.url
        return img 

    def get_html_due_date(self):
        if self.due_date is not None and self.rectification_status == 'uncompleted':
            overdue = ''
            if self.due_date <= timezone.now().date() - timedelta(days=1): # should be 0
                overdue = 'overdue'
            html_text = "<span class='due_date %s'>%s</span>" %(overdue, self.due_date)
        else:
            html_text = "<span class='due_date'></span>"
        return mark_safe(html_text)

    """
    replace by get_xxx_display built-in function

    def get_rectification_status(self):
        return _('Completed') if self.rectification_status == 'completed' else _('Uncompleted')

    def get_location(self):
        for (a,b) in DailyInspection.daily_insepction_location:
            if a == self.location:
                return b
        return None

    def get_category(self):
        for (a,b) in DailyInspection.daily_insepction_category:
            if a == self.category:
                return b
        return None
    """

    def get_impact(self):
        value = ''
        for item in self.impact:
            for (a,b) in DailyInspection.daily_insepction_impact:
                if a == item:
                    if "" == value:
                        value = b
                    else:
                        value = "%s,%s" % (value,b)
                    break
        return value

    def get_created_date(self):
        return self.created.strftime("%Y-%m-%d")

    # can be replaced by field.value_to_string(object)
    def my_get_field_display(self,fieldname):

        if not hasattr(self, fieldname):
            return None
        
        field = DailyInspection._meta.get_field(fieldname)
        return "%s" % self._get_FIELD_display(field)  

    def is_rectification_completed(self)      :
        return self.image_after and hasattr(self.image_after, "url") and self.image_after.url

    def turn_completed(self, instance):
        if self.is_rectification_completed():
            if not instance or not instance.is_rectification_completed():
                return True
        return False

    def rectification_completed_updated(self, instance):
        if self.is_rectification_completed() and instance.is_rectification_completed():
            if not self.image_after.url == instance.image_after.url:
                return True
        return False

    def time_consuming(self):
        return (self.updated-self.created).days

    class Meta:
        verbose_name = _("Daily Inspection")
        verbose_name_plural = _("Daily Inspection")
        ordering = ['-created']



post_delete.connect(file_cleanup, sender=DailyInspection, dispatch_uid="DailyInspection.file_cleanup")
post_save.connect(file_cleanup2, sender=DailyInspection, dispatch_uid="DailyInspection.file_cleanup2")
pre_save.connect(save_raw_instance, sender=DailyInspection)

class DailyInspectionLog(models.Model):
    dailyinspection = models.ForeignKey(DailyInspection, verbose_name=_('Daily Inspection'))
    log = models.CharField(_('log'), max_length=300, blank=False, null=False)

    def __unicode__(self): 
        return ugettext("Daily Inspection") + self.log

class ShelfImport(models.Model):
    shelf_import_file = models.FileField(_("shelf import file"), upload_to='upload/shelf_excel')
    # name = models.CharField(_('name'), max_length=30, blank=True)    

    class Meta:
        ordering = ['shelf_import_file']
        verbose_name = _('shelf import')
        verbose_name_plural =  _('shelf import')

    def __unicode__(self):
        return self.shelf_import_file.name    

class shelf(models.Model):
    type = models.CharField(_('Shelf Type'), max_length=30, blank=True)    
    warehouse = models.CharField(_('Warehouse Number'), max_length=30, blank=True)
    compartment = models.CharField(_('Compartment Number'), max_length=30, blank=True)
    warehouse_channel = models.CharField(_('Warehouse Channel Number'), max_length=30, blank=True)
    group = models.CharField(_('Shelf Group'), max_length=30, blank=True)
    number = models.CharField(_('Shelf Number'), max_length=30, blank=True)    
    is_gradient_measurement_mandatory = models.BooleanField(_('Gradient Measurement Mandatory'), blank=True)

    def __unicode__(self): 
        return "%s-%s-%s" % (self.warehouse,self.compartment, self.number)

    def get_shelf_name(self):
        return _('Shelf')

    def get_absolute_url(self):
        return reverse("shelf_detail", kwargs={"pk": self.id })

    def get_field_name(self):
        return shelf._meta.get_all_field_names()

    def get_fields(self):
        return shelf._meta.get_fields()

    # can be replaced by field.value_to_string(object)
    def my_get_field_display(self,fieldname):

        if not hasattr(self, fieldname):
            return None
        
        field = shelf._meta.get_field(fieldname)
        return "%s" % self._get_FIELD_display(field)

    def is_same_shelf_group(self, instance):
        if instance.get_group_id() == self.get_group_id():
            return True
        return False

    def is_exist(self):
        try:
            if shelf.objects.filter(type=self.type).filter(warehouse=self.warehouse).filter(compartment=self.compartment).\
                filter(warehouse_channel=self.warehouse_channel).filter(group=self.group).filter(number=self.number).filter(is_gradient_measurement_mandatory=self.is_gradient_measurement_mandatory):
                return True
        except:
            pass
        return False

    def get_group_id(self):
        #return[self.type, self.warehouse,self.compartment, self.warehouse_channel,self.group]
        return[self.warehouse,self.compartment, self.warehouse_channel,self.group]

    class Meta:
        verbose_name = _('Shelf')
        verbose_name_plural =  _('Shelf')


class shelf_inspection(models.Model):
    check_date = models.DateField(_('Check Date'),auto_now_add=True, auto_now=False)
    comments = models.TextField(_('Comments'), max_length=30, blank=True, null=True)

    def __unicode__(self): 
        return _("shelf inspection") + " %s" % (self.check_date)

    def get_absolute_url(self):
        return reverse("shelf_inspection_detail_and_record_list_edit", kwargs={"pk": self.id })

    def get_absolute_url_display(self):
        return reverse("shelf_inspection_detail_and_record_list_display", kwargs={"pk": self.id })

    class Meta:
        verbose_name = _("shelf inspection")
        verbose_name_plural = _("shelf inspection")

# class ProductQuerySet(models.query.QuerySet):
#     def active(self):
#         return self.filter(active=True)


# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model, using=self._db)

#     def all(self, *args, **kwargs):
#         return self.get_queryset().active()

#     def get_related(self, instance):
#         products_one = self.get_queryset().filter(categories__in=instance.categories.all())
#         products_two = self.get_queryset().filter(default=instance.default)
#         qs = (products_one | products_two).exclude(id=instance.id).distinct()
#         return qs

class ProductQuerySet(models.query.QuerySet):
    def relevant(self, instance): #instance : one of the upright shelf
        return self.filter(shelf__type=instance.shelf.type).filter(shelf__warehouse=instance.shelf.warehouse).\
                        filter(shelf__warehouse=instance.shelf.compartment).\
                        filter(shelf__warehouse_channel=instance.shelf.warehouse_channel).filter(shelf__group=instance.shelf.group)

    def relevant(self, type, warehouse, warehouse_channel, group): 
        return self.filter(shelf__type=type).filter(shelf__warehouse=warehouse).filter(shelf__warehouse=compartment).\
                        filter(shelf__warehouse_channel=warehouse_channel).filter(shelf__group=group)

    def relevant(self, group_id): 
        #return self.filter(shelf__type=group_id[0]).filter(shelf__warehouse=group_id[1]).filter(shelf__compartment=group_id[2]).\
        #                filter(shelf__warehouse_channel=group_id[3]).filter(shelf__group=group_id[4])
        return self.filter(shelf__warehouse=group_id[0]).filter(shelf__compartment=group_id[1]).\
                        filter(shelf__warehouse_channel=group_id[2]).filter(shelf__group=group_id[3])
class ShelfInspectionRecordManager(models.Manager):
    def relevant(self, *args, **kwargs):
        return self.get_queryset().relevant(*args, **kwargs)

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

class shelf_inspection_record(models.Model):
    shelf_inspection_record_use_condition = (
        ('1', _('Normal')),
        ('2', _('Breakdown')),
    )

    shelf = models.ForeignKey(shelf, verbose_name=_('Shelf'))
    shelf_inspection = models.ForeignKey(shelf_inspection, default=None, verbose_name=_("shelf inspection"))
    use_condition = models.CharField(_('Use Condition'), choices = shelf_inspection_record_use_condition, max_length=30, blank=True) 
    is_locked = models.BooleanField(_('Locked'), blank=True)
    check_person = models.CharField(_('Check Person'), max_length=30, blank=True)
    owner = models.CharField(_('Owner'), max_length=30, blank=True, null=True)
    gradient = models.DecimalField(_('Gradient'), decimal_places=1, max_digits=20, blank=True, null=True)
    check_date = models.DateField(_('Check Date'),auto_now_add=True, auto_now=False)
    forecast_complete_time = models.DateField(_('Forecast Complete Time'), auto_now_add=False, auto_now=False, null=True, blank=True)
    completed_time = models.DateTimeField(_('rectification completed time'), auto_now_add=False, auto_now=False, null=True, blank=True)
    comments = models.TextField(_('Comments'), max_length=30, blank=True,null=True)

    objects = ShelfInspectionRecordManager()

    def __unicode__(self): 
        if self.shelf :
            return _("shelf inspection record") + " %s" % (self.shelf )
        else:
            return _("shelf inspection record") + " %s" % (self.id )

    def get_absolute_url(self):
        return reverse("shelf_inspection_record_detail", kwargs={"pk": self.id })

    def get_absolute_url_update(self):
        return reverse("shelf_inspection_record_update", kwargs={"pk": self.id })

    # can be replaced by field.value_to_string(object)
    # for jason tranmit
    def my_get_field_display(self,fieldname):

        if not hasattr(self, fieldname):
            return None
        
        field = self.__class__._meta.get_field(fieldname)

        if isinstance(field, models.BooleanField):
            if True == getattr(self,fieldname):
                return ugettext("Yes")
            else:
                return ugettext("No")
        else:
            field = shelf_inspection_record._meta.get_field(fieldname)
            return "%s" % self._get_FIELD_display(field)

    def is_normal(self):
        obj=self
        return '1' == obj.use_condition and False == obj.is_locked and obj.gradient < 1.5 and obj.gradient > -1.5

    def turn_normal(self, instance):
        return instance.is_normal() == False and self.is_normal()

    def turn_abnormal(self, instance):
        return instance.is_normal() and self.is_normal() == False

    class Meta:
        verbose_name = _("shelf inspection record")
        verbose_name_plural = _("shelf inspection record")

# class shelf_annual_inspection(models.Model):
#     date = models.DateField(_('Annual Inspection Date'), auto_now_add=False, auto_now=False)
#     next_date = models.DateField(_('Next Inspection Date'), auto_now_add=False, auto_now=False)

#     class Meta:
#         verbose_name = _("shelf annual inspection")

class ShelfAnnualInspection(models.Model):
    shelf = models.ForeignKey(shelf, verbose_name=_("Shelf"))
    date = models.DateField(_('Annual Inspection Date'), auto_now_add=False, auto_now=False)
    next_date = models.DateField(_('Next Inspection Date'), auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = _("shelf annual inspection")
        verbose_name_plural = _("shelf annual inspection")

    def get_absolute_url(self):
        return reverse("shelf_annualinspectin_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("shelf_annualinspectin_update", kwargs={"pk": self.pk })

    def get_absolute_url_list(self):
        return reverse("shelf_annualinspectin_list", kwargs={})


    def __unicode__(self): 
        #return unicode(_("Shelf")) + self.shelf.__unicode__ + unicode(_("Annual Inspection Date"))
        #return "{0}, {1}".format("shelf", self.shelf.__unicode__)
        #return "{0}, {1}".format("shelf", self.shelf.__unicode__)
        return _("shelf annual inspection") + " %s-%s-%s-%s-%s" % (self.shelf.warehouse,self.shelf.compartment, self.shelf.warehouse_channel,self.shelf.group,self.shelf.number)

class ShelfAnnualInspectionImage(models.Model):
    shelf_annual_inspection = models.ForeignKey(ShelfAnnualInspection, verbose_name="shelf annual inspection")
    image = models.ImageField(_('image'), upload_to='inspection/shelf_annual_inspection', blank=False, null=False)

    class Meta:
        verbose_name = _("shelf annual inspection image")
        verbose_name_plural = _("shelf annual inspection image")

    def __unicode__(self): 
        return _("shelf annual inspection image") + " %s" % (self.id )

post_delete.connect(file_cleanup, sender=ShelfAnnualInspectionImage)

class Extinguisher(models.Model):
    name = models.CharField(_('Name'), max_length=30, blank=True)   

    class Meta:
        verbose_name = _("extinguisher")
        verbose_name_plural = _("extinguisher")

    def __unicode__(self): 
        return " %s" % (self.name )

# class ExtinguisherInspection(InspectionMixin):
class ExtinguisherInspection(models.Model):
    equipment_use_condition = [
        ('normal', _('Normal')),
        ('breakdown', _('Breakdown')),
    ]

    extinguisher = models.ForeignKey(Extinguisher, verbose_name=_("extinguisher"))
    capacity = models.CharField(_('Capacity'), max_length=30, blank=True)   
    check_result = models.CharField(_('Check Result'), choices=equipment_use_condition, max_length=30, blank=False, null=False, default="normal")      
    check_person = models.CharField(_('Check Person'), max_length=30, blank=True) 
    owner = models.CharField(_('Owner'), max_length=30, blank=True, null=True)
    forecast_complete_time = models.DateField(_('Forecast Complete Time'), auto_now_add=False, auto_now=False, null=True, blank=True)
    completed_time = models.DateTimeField(_('rectification completed time'), auto_now_add=False, auto_now=False, null=True, blank=True)    
    check_date = models.DateField(_('Check Date'),auto_now_add=True, auto_now=False)


    class Meta:
        verbose_name = _("extinguisher inspection")
        verbose_name_plural = _("extinguisher inspection")
        abstract=False

    def __unicode__(self): 
        return " %s %s" % (self.extinguisher.name, self.check_date )

    def get_absolute_url(self):
        return reverse("extinguisherinspection_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("extinguisherinspection_update", kwargs={"pk": self.pk })

    def get_absolute_url_list(self):
        return reverse("extinguisherinspection_list", kwargs={})

class Hydrant(models.Model):
    name = models.CharField(_('Name'), max_length=30, blank=True) 
    accessories = models.CharField(_('Accessories'), max_length=30, blank=True)   

    class Meta:
        verbose_name = _("hydrant")
        verbose_name_plural = _("hydrant")

    def __unicode__(self): 
        return " %s" % (self.name )

class AbstractEquipment(models.Model):
    hydrant = models.ForeignKey(Hydrant, verbose_name=_("hydrant"))

    class Meta:
        abstract=True

# class HydrantInspection(AbstractEquipment, InspectionMixin):
class HydrantInspection(models.Model):

    equipment_use_condition = [
        ('normal', _('Normal')),
        ('breakdown', _('Breakdown')),
    ]
        
    hydrant = models.ForeignKey(Hydrant, verbose_name=_("hydrant")) 
    check_result = models.CharField(_('Check Result'), choices=equipment_use_condition, max_length=30, blank=False, null=False, default="normal")     
    check_person = models.CharField(_('Check Person'), max_length=30, blank=True) 
    owner = models.CharField(_('Owner'), max_length=30, blank=True, null=True)
    forecast_complete_time = models.DateField(_('Forecast Complete Time'), auto_now_add=False, auto_now=False, null=True, blank=True)
    completed_time = models.DateTimeField(_('rectification completed time'), auto_now_add=False, auto_now=False, null=True, blank=True)    
    check_date = models.DateField(_('Check Date'),auto_now_add=True, auto_now=False)


    class Meta:
        verbose_name = _("hydrant inspection")
        verbose_name_plural = _("hydrant inspection")
        abstract=False

    def __unicode__(self): 
        return " %s %s" % (self.hydrant.name, self.check_date )

    def get_absolute_url(self):
        return reverse("hydrantinspection_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("hydrantinspection_update", kwargs={"pk": self.pk })

    def get_absolute_url_list(self):
        return reverse("hydrantinspection_list", kwargs={})

class Rehearsal(models.Model):
    title = models.CharField(_('Title'), max_length=30, blank=False, null=False)   
    date = models.DateField(_('Date'),auto_now_add=False, auto_now=False)
    attachment = models.FileField(_('Attachment'), blank=True, upload_to='rehearsal') 
    image = models.FileField(_('image'), blank=True, upload_to='rehearsal') 
    
    class Meta:
        verbose_name = _("rehearsal")
        verbose_name_plural = _("rehearsal")

    def get_absolute_url(self):
        return reverse("rehearsal_detail", kwargs={"pk": self.pk })

    def get_absolute_url_list(self):
        return reverse("rehearsal_list", kwargs={})

    def get_absolute_url_update(self):
        return reverse("rehearsal_update", kwargs={"pk": self.pk })
        
    def __unicode__(self): 
        return _("rehearsal") + " %s" % (self.title)

month_choice = (
    ('01', _('January')),
    ('02', _('February')),
    ('03', _('March')),
    ('04', _('April')),
    ('05', _('May')),
    ('06', _('June')),
    ('07', _('July')),
    ('08', _('August')),
    ('09', _('September')),
    ('10', _('October')),
    ('11', _('November')),
    ('12', _('December')),
)


def image_upload_to_pi(instance, filename):
    title, file_extension = filename.split(".")
    if settings.UUSLUGIFY == True:
        new_filename = "%s-%s.%s" %(timezone.now().strftime('%Y%m%d%H%M%S'), uuslugify(title), file_extension)
    else:
        new_filename = "%s-%s.%s" %(timezone.now().strftime('%Y%m%d%H%M%S'), title, file_extension) # created was not ready for CreateView
    print "?"
    print "pi/%s/%s" %(instance.category, new_filename)
    return "pi/%s/%s" %(instance.category, new_filename)

class PI(models.Model):

    PI_company = (
        ('SNT', _('SNT')),
    )

    PI_department = (
        ('security', _('security')),
        ('storage', _('storage')),
        ('administration', _('administration')),
    )

    PI_area = (
        ('inwarehouse', _('in warehouse')),
        ('outwarehouse', _('out warehouse')),
    )

    PI_category = (
        ('PI', _('PI')),
    )

    PI_risk = (
        ('H', 'H'),
        ('M', 'M'),
        ('L', 'L'),
    )

    PI_direct_reason = (
        ('unsafe_condition', _('unsafe condition')),
    )
 
    PI_root_cause = (
        ('MM', _('MM')),
        ('EC', _('EC')),
    )

    PI_correction_status = (
        ('completed', _('Completed')),
        ('uncompleted', _('Uncompleted')),
    )

    
    reporter = models.CharField(_('reporter'), max_length=30, blank=False)
    company_of_reporter = models.CharField(_('company of reporter'), max_length=30, choices = PI_company, blank=False,null=False, default='SNT')
    department_of_reporter = models.CharField(_('department of reporter'), max_length=30, choices = PI_department, blank=False,null=False, default='storage')
    report_content = models.TextField(_('report content'), max_length=500, blank=False,null=False)
    area = models.CharField(_('area'), max_length=30, choices = PI_area, blank=False,null=False, default = 'inwarehouse')
    category = models.CharField(_('category'), max_length=30, choices = PI_category, blank=False,null=False, default='PI')
    risk = models.CharField(_('risk'), max_length=30, choices = PI_risk, blank=False,null=False, default='M')
    direct_reason = models.CharField(_('direct reason'), max_length=30, choices = PI_direct_reason, blank=False,null=False, default='unsafe_condition')
    root_cause = models.CharField(_('root cause'), max_length=30, choices = PI_root_cause, blank=False, default='MM')
    feedback_person = models.CharField(_('feedback person'), max_length=30, blank=False,null=False)
    close_person = models.CharField(_('close person'), max_length=30, blank=True,null=True)
    rectification_measures = models.TextField(_('rectification measures'), max_length=30, blank=False,null=False)
    rectification_status = models.CharField(_('rectification status'), choices = PI_correction_status, max_length=30, blank=False,null=False, default = 'uncompleted')
    created = models.DateTimeField(_('Inspection Created Date'), auto_now_add=True, auto_now=False)
    planned_complete_date = models.DateField(_('planned complete date'), auto_now_add=False, auto_now=False)
    completed_time = models.DateTimeField(_('rectification completed time'), auto_now_add=False, auto_now=False, null=True, blank=True)
    image_before = models.ImageField(_('picture before rectification'), upload_to=image_upload_to_pi, blank=False,null=False)
    image_after = models.ImageField(_('picture after rectification'), upload_to=image_upload_to_pi, null=True, blank=True)

    
    def __unicode__(self): 
        return self.report_content

    def get_absolute_url(self):
        return reverse("pi_detail", kwargs={"pk": self.id })    

    def get_absolute_url_update(self):
        return reverse("pi_update", kwargs={"pk": self.id })    

    def get_absolute_url_list(self):
        return reverse("pi_list", kwargs={})

    def get_html_due_date(self):
        if self.due_date is not None and self.rectification_status == 'uncompleted':
            overdue = ''
            if self.due_date <= timezone.now().date() - timedelta(days=1): # should be 0
                overdue = 'overdue'
            html_text = "<span class='due_date %s'>%s</span>" %(overdue, self.due_date)
        else:
            html_text = "<span class='due_date'></span>"
        return mark_safe(html_text)


    def get_created_date(self):
        return self.created.strftime("%Y-%m-%d")   

    def get_image_url(self, fieldname):
        if hasattr(self, fieldname):
            image = getattr(self,fieldname,None)
            if image:
                return image.url
        return None

    def is_rectification_completed(self):
          return self.get_image_url("image_after")

    class Meta:
        verbose_name = _("PI")
        verbose_name_plural = _("PI")
        ordering = ['-created']

        abstract=True

post_delete.connect(file_cleanup, sender=PI)

class WHPI(PI):
    def get_absolute_url(self):
        return reverse("whpi_detail", kwargs={"pk": self.id })    

    def get_absolute_url_update(self):
        return reverse("whpi_update", kwargs={"pk": self.id })    

    def get_absolute_url_list(self):
        return reverse("whpi_list", kwargs={})

    class Meta:
        verbose_name = _("WHPI")
        verbose_name_plural = _("WHPI")        
        abstract=False

class RTPI(PI):
    def get_absolute_url(self):
        return reverse("rtpi_detail", kwargs={"pk": self.id })    

    def get_absolute_url_update(self):
        return reverse("rtpi_update", kwargs={"pk": self.id })    

    def get_absolute_url_list(self):
        return reverse("rtpi_list", kwargs={})

    class Meta:
        verbose_name = _("RTPI")
        verbose_name_plural = _("RTPI")        
        abstract=False        