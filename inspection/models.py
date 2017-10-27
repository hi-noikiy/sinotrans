from django.db import models
 
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import post_delete, post_save, pre_save
from .utils import file_cleanup, file_cleanup2, save_raw_instance
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.http import Http404
from django.utils import timezone
from datetime import datetime, timedelta
from fields import ThumbnailImageField

# Create your models here.

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
    #new_filename = "%s-%s.%s" %(instance.created.strftime('%Y%m%d%H%M%S'), slugify(title), file_extension)
    new_filename = "%s-%s.%s" %(timezone.now().strftime('%Y%m%d%H%M%S'), slugify(title), file_extension) # created was not ready for CreateView
    return "dailyinspection/%s/%s" %(instance.category, new_filename)

class DailyInspectionManager(models.Manager):
    def external(self, *args, **kwargs):
        #raise Http404
        return super(DailyInspectionManager,self).filter(rectification_status__icontains='uncompleted')
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
        ('3', _('non-conformance 5SS standard')),
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
    rectification_measures = models.TextField(_('Rectification Measures'), max_length=30, blank=False)
    rectification_status = models.CharField(_('Rectification Status'), max_length=30, choices = daily_insepction_correction_status, blank=False, default = 'uncompleted')
    owner = models.CharField(_('Owner'), max_length=30, blank=False)
    due_date = models.DateField(_('Due Date'), auto_now_add=False, auto_now=False)
    created = models.DateTimeField(_('Inspection Created Date'), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(_('Inspection Updated Date'), auto_now_add=False, auto_now=True)
    image_before = ThumbnailImageField(verbose_name = _('Picture before Rectification'), upload_to=image_upload_to_dailyinspection, blank=True, null=True)
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
            if self.due_date <= datetime.now().date() - timedelta(days=1): # should be 0
                overdue = 'overdue'
            html_text = "<span class='due_date %s'>%s</span>" %(overdue, self.due_date)
        else:
            html_text = "<span class='due_date'></span>"
        return mark_safe(html_text)

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

    def get_impact(self):
        value = ''
        for item in self.impact:
            for (a,b) in DailyInspection.daily_insepction_impact:
                if a == item:
                    value = "%s,%s" % (value,b)
                    break
        return value

    def get_created_date(self):
        return self.created.strftime("%Y-%m-%d")

    def get_field_value(self,fieldname):

        if not hasattr(self, fieldname):
            return None
        
        field = DailyInspection._meta.get_field(fieldname)
        return "%s" % self._get_FIELD_display(field)        

    class Meta:
        verbose_name = _("Daily Inspection")
        verbose_name_plural = _("Daily Inspection")
        ordering = ['-created']

post_delete.connect(file_cleanup, sender=DailyInspection, dispatch_uid="DailyInspection.file_cleanup")
post_save.connect(file_cleanup2, sender=DailyInspection, dispatch_uid="DailyInspection.file_cleanup2")
pre_save.connect(save_raw_instance, sender=DailyInspection)


class shelf(models.Model):
    type = models.CharField(_('Shelf Type'), max_length=30, blank=True)    
    warehouse = models.CharField(_('Warehouse Number'), max_length=30, blank=True)
    compartment = models.CharField(_('Compartment Number'), max_length=30, blank=True)
    warehouse_channel = models.CharField(_('Warehouse Channel Number'), max_length=30, blank=True)
    group = models.CharField(_('Shelf Group'), max_length=30, blank=True)
    number = models.CharField(_('Shelf Number'), max_length=30, blank=True)    
    is_gradient_measurement_mandatory = models.BooleanField(_('Gradient Measurement Mandatory'), blank=True)

    def __unicode__(self): 
        return "%s-%s-%s-%s-%s" % (self.warehouse,self.compartment, self.warehouse_channel,self.group,self.number)

    def get_shelf_name(self):
        return _('Shelf')

    def get_absolute_url(self):
        return reverse("shelf_detail", kwargs={"pk": self.id })

    def get_field_name(self):
        return shelf._meta.get_all_field_names()

    def get_fields(self):
        return shelf._meta.get_fields()

    def get_field_value(self,fieldname):

        if not hasattr(self, fieldname):
            return None
        
        field = shelf._meta.get_field(fieldname)
        return "%s" % self._get_FIELD_display(field)

    class Meta:
        verbose_name = _('Shelf')
        verbose_name_plural =  _('Shelf')


class shelf_inspection(models.Model):
    check_date = models.DateField(_('Check Date'),auto_now_add=False, auto_now=False)
    comments = models.TextField(_('Comments'), max_length=30, blank=True, null=True)

    def __unicode__(self): 
        return _("shelf inspection") + " %s %d" % (self.check_date, self.id)

    def get_absolute_url(self):
        return reverse("shelf_inspection_detail", kwargs={"pk": self.id })

    class Meta:
        verbose_name = _("shelf inspection")
        verbose_name_plural = _("shelf inspection")

class shelf_inspection_record(models.Model):
    shelf_inspection_record_use_condition = (
        ('1', _('Normal')),
        ('2', _('Breakdown')),
    )

    shelf = models.ForeignKey(shelf, verbose_name=_('Shelf'))
    shelf_inspection = models.ForeignKey(shelf_inspection, default=None)
    use_condition = models.CharField(_('Use Condition'), choices = shelf_inspection_record_use_condition, max_length=30, blank=True) 
    is_locked = models.BooleanField(_('Locked'), blank=True)
    check_person = models.CharField(_('Check Person'), max_length=30, blank=True)
    gradient = models.DecimalField(_('Gradient'), decimal_places=1, max_digits=20, blank=True, null=True)
    forecast_complete_time = models.DateField(_('Forecast Complete Time'), auto_now_add=False, auto_now=False)
    comments = models.TextField(_('Comments'), max_length=30, blank=True,null=True)

    def __unicode__(self): 
        return _("shelf inspection record") + " %s" % (self.shelf)

    def get_absolute_url(self):
        return reverse("shelf_inspection_record_detail", kwargs={"pk": self.id })

    def get_field_value(self,fieldname):

        if not hasattr(self, fieldname):
            return None
        
        field = self.__class__._meta.get_field(fieldname)
        #if 'is_locked' == fieldname:
        if isinstance(field, models.BooleanField):
            if True == getattr(self,fieldname):
                return "Y"
            else:
                return "N"
        else:
            field = shelf_inspection_record._meta.get_field(fieldname)
            return "%s" % self._get_FIELD_display(field)

    class Meta:
        verbose_name = _("shelf inspection record")
        verbose_name_plural = _("shelf inspection record")

class shelf_annual_inspection(models.Model):
    date = models.DateField(_('Annual Inspection Date'), auto_now_add=False, auto_now=False)
    next_date = models.DateField(_('Next Inspection Date'), auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = _("shelf annual inspection")

class shelf_annual_inspection_image(models.Model):
    shelf_annual_inspection = models.ForeignKey(shelf_annual_inspection)
    image = models.ImageField(_('image'), upload_to='inspection/shelf_annual_inspection', blank=True, null=True)

    class Meta:
        verbose_name = _("shelf annual inspection image")

""" to be delete """
class extinguisher(models.Model):
    name = models.CharField(_('Name'), max_length=30, blank=True)   
    capacity = models.CharField(_('Capacity'), max_length=30, blank=True)   

    class Meta:
        verbose_name = _("extinguisher")

class extinguisher_inspection(models.Model):
    extinguisher = models.ForeignKey(extinguisher)
    check_person = models.CharField(_('Check Person'), max_length=30, blank=True) 
    check_result = models.CharField(_('Check Result'), max_length=30, blank=True) 
    check_date = models.DateField(_('Check Date'),auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = _("extinguisher inspection")


class hydrant(models.Model):
    name = models.CharField(_('Name'), max_length=30, blank=True) 
    accessories = models.CharField(_('Accessories'), max_length=30, blank=True)   

    class Meta:
        verbose_name = _("hydrant")

class hydrant_inspection(models.Model):
    extinguisher = models.ForeignKey(hydrant)
    check_person = models.CharField(_('Check Person'), max_length=30, blank=True) 
    check_result = models.CharField(_('Check Result'), max_length=30, blank=True) 
    check_date = models.DateField(_('Check Date'),auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = _("hydrant inspection")
""" to be delete """

class rehearsal(models.Model):
    title = models.TextField(_('Title'), max_length=30, blank=True)   
    date = models.DateField(_('Date'),auto_now_add=False, auto_now=False)
    attachment = models.FileField(_('Attachment'), blank=True) 
    
    class Meta:
        verbose_name = _("rehearsal")


month_choice = (
    ('1jan', _('January')),
    ('2feb', _('February')),
    ('3mar', _('March')),
    ('4apr', _('April')),
    ('5may', _('May')),
    ('6jun', _('June')),
    ('7jul', _('July')),
    ('8aug', _('August')),
    ('9sep', _('September')),
    ('aoct', _('October')),
    ('bnov', _('November')),
    ('cdev', _('December')),
)

class SprayPumpRoomInspectionManager(models.Manager):
    def get_query_set(self):
        return models.query.QuerySet(self.model, using=self._db)

    def queryset_ordered(self):
        # queryset = []
        # for month in month_choice:
        #     queryset.append(self.get_query_set().filter(month=month[0]))
        # return queryset

        return self.get_query_set().all()

class SprayPumpRoomInspection(models.Model):
    month = models.CharField(_('Month'), choices=month_choice, max_length=30, blank=False,null=False)
    voltage_and_power_normal = models.BooleanField(_('voltage and power normal'), blank=True, default=False)
    indicator_and_instrument_normal = models.BooleanField(_('indicator and instrument normal'), blank=True, default=False)
    inspector = models.CharField(_('Inspector'), max_length=30, blank=False,null=False)
    date_of_inspection = models.DateField(_('Date of Inspection'), auto_now_add=False, auto_now=False,default='1970-01-01')

    objects = SprayPumpRoomInspectionManager()
    def __unicode__(self):
        return _("Spray Pump Room Inspection") + " %s" % (self.month)

    class Meta:
        ordering = ('month',)
        verbose_name = _("Spray Pump Room Inspection")
        verbose_name_plural = _("Spray Pump Room Inspection")
        #unique_together = (('month','yera',),)