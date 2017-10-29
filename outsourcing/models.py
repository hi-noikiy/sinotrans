from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.

RESULT_OPTION = (
    ('yes', _('Yes')),
    ('no', _('No')),
)

def option_value_convertion(tuple_enum,key):
    dict_enum = dict(tuple_enum)
    if key in dict_enum.keys():
        return dict_enum[key]
    else:
        return None

class Forklift(models.Model):
    """docstring for Forklift"""

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
    forklift_length = models.CharField(_('Forklift Length'), max_length=30, blank=False)
    maximum_velocity = models.CharField(_('Maximum Velocity'), max_length=30, blank=False)

    def __unicode__(self): 
        return _("forklift") + self.internal_car_number

    def get_absolute_url(self):
        return reverse("forklift_detail", kwargs={"pk": self.pk })

    class Meta:
        verbose_name = _("forklift")
        verbose_name_plural = _("forklift")

class ForkliftImage(models.Model):
    forklift = models.ForeignKey(Forklift)
    image = models.ImageField(_('image'), upload_to='inspection/forklift', blank=True, null=True)

    class Meta:
        verbose_name = _("forklift image")
        verbose_name_plural = _("forklift image")

    def __unicode__(self): 
        return _("forklift image") + " %s %s" % (self.forklift.internal_car_number, self.id)

class ForkliftMaint(models.Model):
    """docstring for ForkliftMaint"""
    forklift = models.ForeignKey(Forklift, verbose_name=_("forklift"))
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
        return " %s %s %s" % (_("forklift"), self.forklift.internal_car_number , _("Maintenance"))

    """
    def __init__(self, arg):
        super(ForkliftMaint, self).__init__()
        self.arg = arg
    """

    class Meta:
        verbose_name = _("forklift maintenance")
        verbose_name_plural = _("forklift maintenance")

class ForkliftRepair(models.Model):
    forklift = models.ForeignKey(Forklift, verbose_name=_("forklift"))
    damage_reason = models.CharField(_('Damage Reason'), max_length=30, blank=True)
    accessories_name = models.CharField(_('Accessories Name'), max_length=30, blank=True)
    accessories_num = models.DecimalField(_('Accessories Number'), decimal_places=0, max_digits=20, blank=True)
    description = models.TextField(_('Breakdown Description'), max_length=130, blank=False)  
    repaired = models.CharField(_('Repaired'), max_length=30, choices = RESULT_OPTION, blank=True, default = 'no')  
    repaire_date = models.DateField(_('Repaire Date'),auto_now_add=False, auto_now=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = _("forklift repair")
        verbose_name_plural = _("forklift repair")

    def __unicode__(self): 
        return _("forklift repair") + " %s %s" % (self.forklift.internal_car_number, self.repaire_date)

    def get_repaired(self):
        #print self._meta.fields
        return option_value_convertion(RESULT_OPTION, self.repaired)

class ForkliftAnnualInspection(models.Model):
    forklift = models.ForeignKey(Forklift, verbose_name=_("forklift"))
    date = models.DateField(_('Annual Inspection Date'), auto_now_add=False, auto_now=False)
    next_date = models.DateField(_('Next Inspection Date'), auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = _("forklift annual inspection")
        verbose_name_plural = _("forklift annual inspection")


    def __unicode__(self): 
        return " %s %s %s" % (_("forklift"), self.forklift.internal_car_number , _("Annual Inspection Date"))

class ForkliftAnnualInspectionImage(models.Model):
    forklift_annual_inspection = models.ForeignKey(ForkliftAnnualInspection)
    image = models.ImageField(_('image'), upload_to='inspection/forklift_annual_inspection', blank=True, null=True)

    class Meta:
        verbose_name = _("forklift annual inspection image")
        verbose_name_plural = _("forklift annual inspection image")

    def __unicode__(self): 
        return _("forklift annual inspection image") + " %s %s" % (self.forklift_annual_inspection.forklift.internal_car_number, self.id)