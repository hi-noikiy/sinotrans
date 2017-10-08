from django.db import models
 
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import post_delete, post_save, pre_save
from .utils import file_cleanup, file_cleanup2, save_raw_instance
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
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
        return _("Daily Inspection ") + self.inspection_content

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


class forklift(models.Model):
    """docstring for forklift"""

    internal_car_number = models.CharField(_('Inner Car Number'), max_length=30, blank=False)
    internal_plate_number = models.CharField(_('Inner Plate Number'), max_length=30, blank=False)
    model = models.CharField(_('Forklift Model'), max_length=30, blank=False)
    sn = models.CharField(_('SN'), max_length=30, blank=False)
    category = models.CharField(_('Forklift Category'), max_length=30, blank=False)
    manufacturer = models.CharField(_('Manufacturer'), max_length=30, blank=False)
    tip_height = models.CharField(_('Tip Height'), max_length=30, blank=False)
    carrying_capacity = models.CharField(_('Carrying Capacity'), max_length=30, blank=False)
    self_weight = models.CharField(_('Self Weight'), max_length=30, blank=False)
    turning_radius = models.CharField(_('Turning Radius'), max_length=30, blank=False)
    front_tyre_size = models.CharField(_('Front Tyre Size'), max_length=30, blank=False)
    back_tyre_size = models.CharField(_('Back Tyre Size'), max_length=30, blank=False)
    width = models.CharField(_('Forklift Width'), max_length=30, blank=False)
    length = models.CharField(_('Forklift Length'), max_length=30, blank=False)
    fork_length = models.CharField(_('Fork Length'), max_length=30, blank=False)
    maximum_velocity = models.CharField(_('Maximum Velocity'), max_length=30, blank=False)

    def __unicode__(self): 
        return _("forklift") + self.internal_car_number

    class Meta:
        verbose_name = _("forklift")
        verbose_name_plural = _("forklift")

class forklift_image(models.Model):
    forklift = models.ForeignKey(forklift)
    image = models.ImageField(_('image'), upload_to='inspection/forklift', blank=True, null=True)

    class Meta:
        verbose_name = _("forklift image")
        verbose_name_plural = _("forklift image")

class forklift_maint(models.Model):
    """docstring for forklift_maint"""
    clean_forklift = models.CharField(_('clean forklift'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    clean_and_lubricate_chain = models.CharField(_('clean and lubricate chain'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    lubricate_gateshelf_and_lean_cylinder_bearing = models.CharField(_('lubricate gateshelf and lean cylinder bearing'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    lubricate_sideswayfork_and_check_work_status = models.CharField(_('lubricate sideswayfork and check work status'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    fastening_tyre_nut = models.CharField(_('fastening tyre nut'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_tyre_status = models.CharField(_('check tyre status'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_gear_oil_level_and_leak = models.CharField(_('check gear oil level and leak'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_hydraulic_oil_level = models.CharField(_('check hydraulic oil level'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    clean_all_motor_and_accessories = models.CharField(_('clean all motor and accessories'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_and_clean_motor_cooling_fan = models.CharField(_('check and clean motor cooling fan'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_all_cable_and_connection_status = models.CharField(_('check all cable and connection status'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_battery_electrolyte_liquidometer_ratio = models.CharField(_('check battery electrolyte liquidometer ratio'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_charger_status = models.CharField(_('check charger status'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_pipeline_fastening_and_leak = models.CharField(_('check pipeline fastening and leak'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_pallet_fork_and_pin_lock = models.CharField(_('check pallet fork and pin lock'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_lubricate_pedal_and_control_linkage = models.CharField(_('check lubricate pedal and control linkage'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_braking_device = models.CharField(_('check braking device'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_all_motor_carbon_brush = models.CharField(_('check all motor carbon brush'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_overhead_guard_and_counter_weight = models.CharField(_('check overhead guard and counter weight'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_steering_axle_and_drive_axle = models.CharField(_('check steering axle and drive axle'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_gateshelf_and_chain = models.CharField(_('check gateshelf and chain'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_hub_bearing = models.CharField(_('check hub bearing'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_steering_axle_bearing = models.CharField(_('check steering axle bearing'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    check_gateshlf_bearing = models.CharField(_('check gateshlf bearing'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    change_gear_oil = models.CharField(_('change gear oil'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    change_oil_suction_filter = models.CharField(_('change oil suction filter'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    change_ventilate_filter = models.CharField(_('change ventilate filter'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    change_hydraulic_oil = models.CharField(_('change hydraulic oil'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): 
        return _("forklift") + self.internal_car_number

    def __init__(self, arg):
        super(forklift_maint, self).__init__()
        self.arg = arg

    class Meta:
        verbose_name = _("forklift maintenance")
        verbose_name_plural = _("forklift maintenance")

class forklift_repair(models.Model):
    damage_reason = models.CharField(_('Damage Reason'), max_length=30, blank=True)
    accessories_name = models.CharField(_('Accessories Name'), max_length=30, blank=True)
    accessories_num = models.DecimalField(_('Accessories Number'), decimal_places=0, max_digits=20, blank=True)
    description = models.TextField(_('Description'), max_length=30, blank=False)  
    repaired = models.CharField(_('Repaired'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')  
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = _("forklift repair")
        verbose_name_plural = _("forklift repair")

class forklift_annual_inspection(models.Model):
    date = models.DateField(_('Annual Inspection Date'), auto_now_add=False, auto_now=False)
    next_date = models.DateField(_('Next Inspection Date'), auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = _("forklift annual inspection")
        verbose_name_plural = _("forklift annual inspection")

class forklift_annual_inspection_image(models.Model):
    forklift = models.ForeignKey(forklift_annual_inspection)
    image = models.ImageField(_('image'), upload_to='inspection/forklift_annual_inspection', blank=True, null=True)

    class Meta:
        verbose_name = _("forklift annual inspection image")
        verbose_name_plural = _("forklift annual inspection image")

'''
class warehouse(models.Model):
    warehouse = models.CharField(_('Warehouse Number'), max_length=30, blank=True)

class compartment(models.Model):
    compartment = models.CharField(_('Compartment Number'), max_length=30, blank=True)

class warehouse_channel(models.Model):
    warehouse_channel = models.CharField(_('Warehouse Channel Number'), max_length=30, blank=True)
'''

class shelf(models.Model):
    type = models.CharField(_('Shelf Type'), max_length=30, blank=True)    
    warehouse = models.CharField(_('Warehouse Number'), max_length=30, blank=True)
    compartment = models.CharField(_('Compartment Number'), max_length=30, blank=True)
    warehouse_channel = models.CharField(_('Warehouse Channel Number'), max_length=30, blank=True)
    group = models.CharField(_('Shelf Group'), max_length=30, blank=True)
    number = models.CharField(_('Shelf Number'), max_length=30, blank=True)    
    is_gradient_measurement_mandatory = models.BooleanField(_('Gradient Measurement Mandatory'), blank=True)

    def __unicode__(self): 
        return "%s %s %s %s %s" % (self.warehouse,self.compartment, self.warehouse_channel,self.group,self.number)

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

    shelf = models.ForeignKey(shelf)
    shelf_inspection = models.ForeignKey(shelf_inspection, default=None)
    use_condition = models.CharField(_('Use Condition'), choices = shelf_inspection_record_use_condition, max_length=30, blank=True) 
    is_locked = models.BooleanField(_('Locked'), blank=True)
    check_person = models.CharField(_('Check Person'), max_length=30, blank=True)
    gradient = models.DecimalField(_('Gradient'), decimal_places=1, max_digits=20, blank=True, null=True)
    forecast_complete_time = models.DateField(_('Forecast Complete Time'), auto_now_add=False, auto_now=False)
    comments = models.TextField(_('Comments'), max_length=30, blank=True,null=True)

    def __unicode__(self): 
        return _("shelf inspection record ") + "%s" % (self.shelf)

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

class rehearsal(models.Model):
    title = models.TextField(_('Title'), max_length=30, blank=True)   
    date = models.DateField(_('Date'),auto_now_add=False, auto_now=False)
    attachment = models.FileField(_('Attachment'), blank=True) 
    
    class Meta:
        verbose_name = _("rehearsal")

class equipment(models.Model):
    equipment_type = (
        ('electrical equipment', _('electrical equipment')),
        ('emergency exit door', _('emergency exit door')),
        ('emergency lamp', _('emergency lamp')),
        ('entrance door', _('entrance door')),
        ('downpipe', _('downpipe')),
        ('fireproof door', _('fireproof door')),
    )

    name = models.CharField(_('Name'), max_length=30, blank=False, null=False) # name can include location
    type = models.CharField(_('Type'), choices = equipment_type, max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = _('equipment')

    def __unicode__(self):
        return "%s" % (self.name)

class equipment_inspection(models.Model):
    equipment_use_condition = (
        ('normal', _('Normal')),
        ('breakdown', _('Breakdown')),
    )

    equipment = models.ForeignKey(equipment)
    use_condition = models.CharField(_('Use Condition'), choices=equipment_use_condition, max_length=30, blank=False,null=False,default='normal')
    inspector = models.CharField(_('Inspector'), max_length=30, blank=False,null=False)
    date_of_inspection = models.DateField(_('Date of Inspection'), auto_now_add=False, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('equipment inspection')
        abstract = True
        unique_together = (('equipment','inspector','date_of_inspection'),)

    def get_absolute_url(self):
        return reverse("electronialequipmentinsepction_detail", kwargs={"pk": self.id})

class ElectricalEquipmentInspectionManager(models.Manager):
    def get_query_set(self):
        return models.query.QuerySet(self.model, using=self._db)

    def get_this_day(self):
        start = timezone.now().date()
        end = start + timedelta(days=1)

        return self.get_query_set().filter(date_of_inspection__range=(start, end))


class ElectricalEquipmentInspection(equipment_inspection):
    objects = ElectricalEquipmentInspectionManager()

    class Meta:
        abstract = False
        unique_together = (('equipment','inspector','date_of_inspection'),)

    def __unicode__(self):
        return "%s" % (self.equipment.name)