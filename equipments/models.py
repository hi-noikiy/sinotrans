from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save

from inspection.models import month_choice, DailyInspection
from inspection.utils import PercentageField
# Create your models here.
class EquipmentType(models.Model):
    
    name = models.CharField(_('Name'), max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = _('Equipment Type')
        verbose_name_plural = _('Equipment Type')

    def __unicode__(self):
        return "%s" % (self.name)

class Equipment(models.Model):

    name = models.CharField(_('Name'), max_length=30, blank=False, null=False) 
    type = models.ForeignKey(EquipmentType, verbose_name = _('Type'))

    class Meta:
        verbose_name = _('Equipment')
        verbose_name_plural = _('Equipment')

    def __unicode__(self):
        return "%s" % (self.name) 

class AbstractEquipmentInspection(models.Model):
    equipment_use_condition = [
        ('normal', _('Normal')),
        ('breakdown', _('Breakdown')),
    ]

    equipment = models.ForeignKey(Equipment, verbose_name=_('Equipment'))
    use_condition = models.CharField(_('Use Condition'), choices=equipment_use_condition, max_length=30, blank=False,null=False,default='normal')
    inspector = models.CharField(_('Inspector'), max_length=30, blank=False,null=False)
    owner = models.CharField(_('Owner'), max_length=30, blank=True, null=True)
    comments = models.TextField(_('Comments'), max_length=130, blank=True, null=True)   
    check_date = models.DateField(_('Date of Inspection'), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(_('Latest Update'),auto_now_add=False, auto_now=True)
    due_date = models.DateField(_('Due Date'), auto_now_add=False, auto_now=False, null=True, blank=True)
    completed_time = models.DateTimeField(_('rectification completed time'), auto_now_add=False, auto_now=False, null=True, blank=True)

    class Meta:
        verbose_name = _('Equipment Inspection')
        verbose_name_plural = _('Equipment Inspection')
        abstract = True
        unique_together = (('equipment','inspector','check_date'),)

    def get_absolute_url(self):
        return reverse("equipmentinsepction_detail", kwargs={"pk": self.id})    

    def get_use_condition(self):
        return _('Normal') if self.use_condition == 'normal' else _('Breakdown')

    def time_consuming(self):
        return (self.updated.replace(tzinfo=None) - datetime.strptime(str(self.check_date),'%Y-%m-%d').replace(tzinfo=None)).days

        
class EquipmentInspectionManager(models.Manager):
    def get_query_set(self):
        return models.query.QuerySet(self.model, using=self._db)

    def get_this_day(self):
        start = timezone.now().date()
        end = start + timedelta(days=1)

        return self.get_query_set().filter(check_date__range=(start, end))


class EquipmentInspection(AbstractEquipmentInspection):
    objects = EquipmentInspectionManager()

    class Meta:
        abstract = False
        verbose_name = _('Equipment Inspection')
        verbose_name_plural = _('Equipment Inspection')
        
    def __unicode__(self):
        return "%s" % (self.equipment.name)    

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
    year = models.PositiveIntegerField(_("year"),
        validators=[MinValueValidator(2000), MaxValueValidator(timezone.now().year+1)],
        blank=False,null=False, help_text=_("Use the following format: < YYYY >"))
    month = models.CharField(_('Month'), choices=month_choice, max_length=30, blank=False,null=False)
    voltage_and_power_normal = models.BooleanField(_('voltage and power normal'), blank=True, default=False)
    indicator_and_instrument_normal = models.BooleanField(_('indicator and instrument normal'), blank=True, default=False)
    switch_contactor_and_connection_normal = models.BooleanField(_('switch contactor and connection normal'), blank=True, default=False)
    no_corrosion_inside_and_foundation_bolt_not_loose = models.BooleanField(_('no corrosion inside and foundation bolt not loose'), blank=True, default=False)
    motor_and_pump_connection_intact = models.BooleanField(_('motor and pump connection intact'), blank=True, default=False)
    motor_sample_integrated = models.BooleanField(_('motor sample integrated'), blank=True, default=False)
    no_corrosion_and_damage = models.BooleanField(_('no corrosion and damage'), blank=True, default=False)
    valve_normally_open = models.BooleanField(_('valve normally open'), blank=True, default=False)
    one_way_valve_intact_and_no_leak_and_pressure_gage_normal = models.BooleanField(_('one-way valve intact and no leak and pressure gage normal'), blank=True, default=False)
    pressure_maintaining_valve_intact = models.BooleanField(_('pressure maintaining valve intact'), blank=True, default=False)
    water_level_normal_and_moisturizing_well = models.BooleanField(_('water level normal and moisturizing well'), blank=True, default=False)
    water_level_cover_plate_and_no_abnormal_move = models.BooleanField(_('water level cover plate and no abnormal move'), blank=True, default=False)
    pool_wall_dry_and_no_leak = models.BooleanField(_('pool wall dry and no leak'), blank=True, default=False)
    no_sundries_in_pump_house = models.BooleanField(_('no sundries in pump house'), blank=True, default=False)
    pump_house_clean_and_tidy = models.BooleanField(_('pump house clean and tidy'), blank=True, default=False)

    rectification_status = models.CharField(_('Rectification Status'), max_length=30, choices = DailyInspection.daily_insepction_correction_status, blank=False, default = 'uncompleted')
    owner = models.CharField(_('Owner'), max_length=30, blank=False, null=False)
    inspector = models.CharField(_('Inspector'), max_length=30, blank=False,null=False)
    check_date = models.DateField(_('Date of Inspection'), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(_('updated'),auto_now_add=False, auto_now=True)

    objects = SprayPumpRoomInspectionManager()
    def __unicode__(self):
        return _("Spray Pump Room Inspection") + " %s" % (self.month)

    class Meta:
        ordering = ('month',)
        verbose_name = _("Spray Pump Room Inspection")
        verbose_name_plural = _("Spray Pump Room Inspection")
        unique_together = (('month','year',),)        

    def get_absolute_url(self):
        return reverse("spraypumproominspection_detail", kwargs={"pk": self.id })

    def get_absolute_url_update(self):
        return reverse("spraypumproominspection_update", kwargs={"pk": self.id }) 

    def get_list_display(self):
        return reverse("spraypumproominspection_list_display", kwargs={}) 

    def get_list_edit(self):
        return reverse("spraypumproominspection_list_edit", kwargs={}) 

    def get_create_url(self, year, month):
        return reverse("spraypumproominspection_create", kwargs={"year": year,"month": month })

    def is_rectification_completed(self):
        is_completed = True
        for fieldname in self.__class__._meta.get_all_field_names():
            field = self.__class__._meta.get_field(fieldname)

            if field and isinstance(field, models.BooleanField):
                f = getattr(self, fieldname)
                if not f:
                    is_completed = False
                    break
        return is_completed

    def time_consuming(self):
        return (self.updated.replace(tzinfo=None) - datetime.strptime(str(self.check_date),'%Y-%m-%d').replace(tzinfo=None)).days

class SprayWarehouseInspection(models.Model):
    year = models.PositiveIntegerField(_("year"),
        validators=[MinValueValidator(2000), MaxValueValidator(timezone.now().year+1)],
        blank=False,null=False, help_text=_("Use the following format: < YYYY >"))
    month = models.CharField(_('Month'), choices=month_choice, max_length=30, blank=False,null=False)
    valve_normal = models.BooleanField(_('valve normal'), blank=True, default=False)
    valve_open_signal_transmission_normal  = models.BooleanField(_('valve open signal transmission normal '), blank=True, default=False)
    valve_no_corrosion = models.BooleanField(_('valve no corrosion'), blank=True, default=False)
    water_testing_normal = models.BooleanField(_('water testing normal'), blank=True, default=False)
    valve_switch_in_close_status = models.BooleanField(_('valve switch in close status'), blank=True, default=False)
    pipe_network_pressure_normal = models.BooleanField(_('pipe network pressure normal'), blank=True, default=False)
    pipe_valve_in_open_status = models.BooleanField(_('pipe valve in open status'), blank=True, default=False)
    pipe_connection_no_leakage = models.BooleanField(_('pipe connection no leakage'), blank=True, default=False)
    spray_head_no_leakage = models.BooleanField(_('spray head no leakage'), blank=True, default=False)

    rectification_status = models.CharField(_('Rectification Status'), max_length=30, choices = DailyInspection.daily_insepction_correction_status, blank=False, default = 'uncompleted')
    owner = models.CharField(_('Owner'), max_length=30, blank=False, null=False)

    inspector = models.CharField(_('Inspector'), max_length=30, blank=False,null=False)
    check_date = models.DateField(_('Date of Inspection'), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(_('updated'), auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return _("Spray Warehouse Inspection") + " %s" % (self.month)

    class Meta:
        ordering = ('month',)
        verbose_name = _("Spray Warehouse Inspection")
        verbose_name_plural = _("Spray Warehouse Inspection")
        unique_together = (('month','year',),)        

    def get_absolute_url(self):
        return reverse("spraywarehouseinspection_detail", kwargs={"pk": self.id })    

    def get_absolute_url_update(self):
        return reverse("spraywarehouseinspection_update", kwargs={"pk": self.id })


    def get_list_display(self):
        return reverse("spraywarehouseinspection_list_display", kwargs={}) 

    def get_list_edit(self):
        return reverse("spraywarehouseinspection_list_edit", kwargs={}) 

    def get_create_url(self, year, month):
        return reverse("spraywarehouseinspection_create", kwargs={"year": year,"month": month  })  

    def is_rectification_completed(self):
        is_completed = True
        for fieldname in self.__class__._meta.get_all_field_names():
            field = self.__class__._meta.get_field(fieldname)

            if field and isinstance(field, models.BooleanField):
                f = getattr(self, fieldname)
                if not f:
                    is_completed = False
                    break
        return is_completed

    def time_consuming(self):
        return (self.updated.replace(tzinfo=None) - datetime.strptime(str(self.check_date),'%Y-%m-%d').replace(tzinfo=None)).days

def save_rectification_status(sender, instance, *args, **kwargs):
    if instance.is_rectification_completed():
        instance.rectification_status = 'completed'
    else:
        instance.rectification_status = 'uncompleted'

pre_save.connect(save_rectification_status, sender=SprayPumpRoomInspection)
pre_save.connect(save_rectification_status, sender=SprayWarehouseInspection)

class HSSEKPI(models.Model):
    year = models.PositiveIntegerField(_("year"),
        validators=[MinValueValidator(2000), MaxValueValidator(timezone.now().year+1)],
        blank=False,null=False, help_text=_("Use the following format: < YYYY >"))
    month = models.CharField(_('Month'), choices=month_choice, max_length=30, blank=False, null=False)
    LTI = models.PositiveIntegerField(_('LTI'), blank=False, null=False, default=0)
    RWC  = models.PositiveIntegerField(_('RWC - restricted working cases'), blank=False, null=False, default=0)
    MTC = models.PositiveIntegerField(_('MTC - medical treatment cases'), blank=False, null=False, default=0)
    FAC = models.PositiveIntegerField(_('FAC'), blank=False, null=False, default=0)
    LPOC = models.PositiveIntegerField(_('LPOC'), blank=False, null=False, default=0)
    cargo_lost_liter = models.PositiveIntegerField(_('cargo lost liter'), blank=False, null=False, default=0)
    TRC = models.PositiveIntegerField(_('TRC'), blank=False, null=False, default=0)
    LSR_violation_case_count = models.PositiveIntegerField(_('LSR violation case count'), blank=False, null=False, default=0)
    PI_NM_reported_count = models.PositiveIntegerField(_('PI NM reported count'), blank=False, null=False, default=0)
    best_PI_NM_report_count = models.PositiveIntegerField(_('best PI NM report count'), blank=False, null=False, default=0)
    PI_NM_close_rate = PercentageField(_('PI NM close rate'), blank=False, null=False, max_length=30, default='0%')
    leadship_SSWT_ongoing_count = models.PositiveIntegerField(_('leadship SSWT ongoing count'), blank=False, null=False, default=0)
    leadship_SSWT_close_rate = PercentageField(_('leadship SSWT close rate'), blank=False, null=False, max_length=30, default='0%')
    annual_plan_execution_rate = PercentageField(_('annual plan execution rate'), blank=False, null=False, max_length=30, default='0%')
    save_working_hours = models.PositiveIntegerField(_('save working hours'), blank=False, null=False, default=0)

    inspector = models.CharField(_('Inspector'), max_length=30, blank=False,null=False)
    created = models.DateTimeField(_('Date of Inspection'), auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return _("HSSE KPI") + " %s" % (self.month)

    class Meta:
        ordering = ('month',)
        verbose_name = _("HSSE KPI")
        verbose_name_plural = _("HSSE KPI")
        unique_together = (('month','year',),)        

    def get_absolute_url(self):
        return reverse("hssekpi_detail", kwargs={"pk": self.id })    

    def get_absolute_url_update(self):
        return reverse("hssekpi_update", kwargs={"pk": self.id })


    def get_list_display(self):
        return reverse("hssekpi_list_display", kwargs={}) 

    def get_list_edit(self):
        return reverse("hssekpi_list_edit", kwargs={}) 

    def get_create_url(self, year, month):
        return reverse("hssekpi_create", kwargs={"year": year,"month": month  })           
