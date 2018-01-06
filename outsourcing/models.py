from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from datetime import datetime, timedelta
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from inspection.models import month_choice
from inspection.utils import valid_percentage
from inspection.utils import PercentageField


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

    internal_car_number = models.CharField(_('Inner Car Number'), max_length=30, blank=False, unique=True)
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
    forklift_length = models.CharField(_('Fork Length'), max_length=30, blank=False)
    maximum_velocity = models.CharField(_('Maximum Velocity'), max_length=30, blank=False)

    def __unicode__(self): 
        return _("forklift") + self.internal_car_number

    def get_absolute_url(self):
        return reverse("forklift_detail", kwargs={"pk": self.pk })

    '''
    def get_absolute_url_update(self):
        return reverse("forklift_update", kwargs={"pk": self.pk })
    '''

    def get_absolute_url_list(self):
        return reverse("forklift_list", kwargs={ })
        
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
    created = models.DateTimeField(_('Create Date'),auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(_('Latest Update'),auto_now_add=False, auto_now=True)
    expense = models.DecimalField(_('Expense'), decimal_places=2, max_digits=20, blank=False, null=False, default=0)

    def __unicode__(self): 
        return " %s %s %s" % (_("forklift"), self.forklift.internal_car_number , _("Maintenance"))

    def get_absolute_url(self):
        return reverse("forklift_maint_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("forklift_maint_update", kwargs={"pk": self.pk })

    def get_absolute_url_list(self):
        return reverse("forklift_maint_list", kwargs={})
        
    class Meta:
        verbose_name = _("forklift maintenance")
        verbose_name_plural = _("forklift maintenance")

class ForkliftRepair(models.Model):
    forklift = models.ForeignKey(Forklift, verbose_name=_("forklift"))
    damage_reason = models.CharField(_('Damage Reason'), max_length=30, blank=False, null=False)
    accessories_name = models.CharField(_('Accessories Name'), max_length=30, blank=False, null=False)
    accessories_num = models.DecimalField(_('Accessories Number'), decimal_places=0, max_digits=20, blank=False, null=False)
    description = models.TextField(_('Breakdown Description'), max_length=130, blank=False, null=False)  
    repaired = models.CharField(_('Repaired'), max_length=30, choices = RESULT_OPTION, blank=False, null=False, default = 'no')  
    repaire_date = models.DateField(_('Repaire Date'),auto_now_add=False, auto_now=False, null=True, blank=True)
    created = models.DateTimeField(_('Discovered Date'),auto_now_add=True, auto_now=False)
    due_date = models.DateField(_('Due Date'), auto_now_add=False, auto_now=False, null=True, blank=True)
    owner = models.CharField(_("Owner"), blank=False, null=False, max_length=30)
    updated = models.DateTimeField(_('updated'),auto_now_add=False, auto_now=True)
    expense = models.DecimalField(_('Expense'), decimal_places=2, max_digits=20, blank=False, null=False, default=0)

    class Meta:
        verbose_name = _("forklift repair")
        verbose_name_plural = _("forklift repair")

    def __unicode__(self): 
        #return _("forklift repair") + " %s %s" % (self.forklift.internal_car_number, self.created.strftime('%Y-%m-%d %H:%M:%S')) # timezone issue
        return _("forklift repair") + " %s %s" % (self.forklift.internal_car_number, self.created.strftime('%Y-%m-%d'))

    def is_repaired(self):
        return self.repaired == "yes"

    def get_absolute_url(self):
        return reverse("forklift_repair_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("forklift_repair_update", kwargs={"pk": self.pk })
        
    def get_absolute_url_list(self):
        return reverse("forklift_repair_list", kwargs={})
        
    """
    replace by built-in function get_repaired_display
    def get_repaired(self):
        return option_value_convertion(RESULT_OPTION, self.repaired)
    """

class ForkliftAnnualInspection(models.Model):
    forklift = models.ForeignKey(Forklift, verbose_name=_("forklift"))
    date = models.DateField(_('Annual Inspection Date'), auto_now_add=False, auto_now=False)
    next_date = models.DateField(_('Next Inspection Date'), auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = _("forklift annual inspection")
        verbose_name_plural = _("forklift annual inspection")

    def get_absolute_url(self):
        return reverse("forklift_annual_inspection_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("forklift_annual_inspection_update", kwargs={"pk": self.pk })
        
    def get_absolute_url_list(self):
        return reverse("forklift_annual_inspection_list", kwargs={})
        
    def __unicode__(self): 
        return " %s %s %s" % (_("forklift"), self.forklift.internal_car_number , _("Annual Inspection Date"))

class ForkliftAnnualInspectionImage(models.Model):
    forklift_annual_inspection = models.ForeignKey(ForkliftAnnualInspection)
    image = models.ImageField(_('image'), upload_to='inspection/forklift_annual_inspection', blank=False, null=False)

    class Meta:
        verbose_name = _("forklift annual inspection image")
        verbose_name_plural = _("forklift annual inspection image")

    def __unicode__(self): 
        return _("forklift annual inspection image") + " %s %s" % (self.forklift_annual_inspection.forklift.internal_car_number, self.id)


class Vehicle(models.Model):
    SERVICE_CONTENT_OPTION = (
        ('shuttle bus', _('shuttle bus')),
        ('truck', _('truck')),
        ('dangerous goods vehicles', _('dangerous goods vehicles')),
        ('scattered oil vehicles', _('scattered oil vehicles')),        
    )

    service_content = models.CharField(_("service content"), choices=SERVICE_CONTENT_OPTION, max_length=130, blank=False, null=False)
    relevant_license_plate = models.CharField(_("relevant license plate"), max_length=30, blank=False, null=False)
    vehicle_inspection_valid_until = models.DateField(_("vehicle inspection valid until"), blank=False, null=False,auto_now=False, auto_now_add=False)
    vehicle_type = models.CharField(_("vehicle type"), max_length=30, blank=False, null=False)
    relevant_trailer_number = models.CharField(_("relevant trailer number"), max_length=30, blank=False, null=False)
    trailer_inspection_valid_until = models.DateField(_("trailer inspection valid until"),  blank=False, null=False,auto_now=False, auto_now_add=False)
    maximum_loadable_tonnage = models.PositiveIntegerField(_("maximum loadable tonnage"), blank=False, null=False)
    green_mark_valid_until = models.DateField(_("green mark valid until"), blank=False, null=False,auto_now=False, auto_now_add=False)
    insurance_policy_valid_until = models.DateField(_("insurance policy valid until"), blank=False, null=False,auto_now=False, auto_now_add=False)
    GPS = models.CharField(_("GPS"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    ABS = models.CharField(_("ABS"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    antiroll_protection = models.CharField(_("antiroll protection"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    reversing_alarm = models.CharField(_("reversing alarm"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    side_edge_and_low_location_collision_guard_bar = models.CharField(_("side edge and low location collision guard bar"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    car_seat_headrest = models.CharField(_("car seat headrest"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    three_point_belt = models.CharField(_("three-point belt"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    IVMS_or_VDR = models.CharField(_("IVMS or VDR"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    anti_drop_equipment = models.CharField(_("anti-drop equipment"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    
    class Meta:
        verbose_name = _("vehicle")
        verbose_name_plural = _("vehicles")

    def __unicode__(self): 
        return _("vehicle") + " %s" % (self.relevant_license_plate)
        
    def get_absolute_url(self):
        return reverse("vehicle_detail", kwargs={"pk": self.pk })

    def get_absolute_url_list(self):
        return reverse("vehicle_list", kwargs={})
        
class Driver(models.Model):
    #vehicle = models.ForeignKey(Vehicle, verbose_name=_("vehicle"), blank=True, null=True )
    name = models.CharField(_("name"), max_length=30, blank=False, null=False)
    driver_ID = models.CharField(_("Driver ID"), max_length=30, blank=False, null=False)
    driver_license_type = models.CharField(_("driver license type"), max_length=30, blank=False, null=False)
    DDC_certificate_number = models.CharField(_("DDC certificate number"), max_length=30, blank=False, null=False)
    certificate_issued_time = models.DateField(_("certificate issued time"),  blank=False, null=False,auto_now=False, auto_now_add=False)
    certificate_valid_until = models.DateField(_("certificate valid until"),  blank=False, null=False,auto_now=False, auto_now_add=False)
    first_licensed_time = models.DateField(_("first licensed time"),  blank=False, null=False,auto_now=False, auto_now_add=False)    
    driving_years = models.PositiveIntegerField(_("dirving years"), blank=False, null=False)
    driver_license_valid_until = models.DateField(_("driver license valid until"),  blank=False, null=False,auto_now=False, auto_now_add=False)
    contact_phone = models.CharField(_("contact phone"), max_length=30, blank=False, null=False)
    training_qualified = models.CharField(_("training qualified"), choices = RESULT_OPTION, max_length=30, blank=False, null=False)
    motorcade = models.CharField(_("motorcade"), max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = _("driver")
        verbose_name_plural = _("drivers")

    def __unicode__(self): 
        #return _("driver") + " %s %s" % (self.name, self.driver_ID)
        return " %s %s" % (self.name, self.driver_ID)

    def get_absolute_url(self):
        return reverse("driver_detail", kwargs={"pk": self.pk })

    def get_absolute_url_list(self):
        return reverse("driver_list", kwargs={})
        
class VehicleInspection(models.Model):
    load_or_unload = (
        ('load', _('load cargo')),
        ('unload', _('unload cargo')),
    )

    vehicle = models.ForeignKey(Vehicle, verbose_name=_("vehicle") )
    driver = models.ForeignKey(Driver, verbose_name=_("driver")) 
    created = models.DateTimeField(_("Date of Inspection"), blank=False, null=False,auto_now=False, auto_now_add=True)
    inspector = models.CharField(_("Inspector"), blank=False, null=False, max_length=30)
    owner = models.CharField(_("Owner"), blank=False, null=False, max_length=30)
    load_or_unload = models.CharField(_("load or unload"), choices = load_or_unload, blank=False, null=False, max_length=30, default='load')
    carrier = models.CharField(_("carrier"), blank=False, null=False,max_length=30)
    disqualification_comments = models.TextField(_("disqualification comments"), blank=False, null=False,max_length=300)
    rectification_qualified = models.CharField(_("Rectification qualified"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    hardware_inspection_disqualification = models.CharField(_("hardware inspection disqualification"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    no_driver_code_of_conduct = models.CharField(_("no driver code of conduct"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    overload_or_LSR_violation = models.CharField(_("overload or LSR violation"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    safety_policy_violation = models.CharField(_("safety policy violation"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    no_journey_plan_or_log = models.CharField(_("no journey plan or log"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    vehichle_not_register = models.CharField(_("vehichle not register"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    no_vehicle_inspection_record = models.CharField(_("no vehicle inspection record"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    no_DDC_certificate = models.CharField(_("no DDC certificate"), choices = RESULT_OPTION, blank=False, null=False,max_length=30, default="no")
    due_date = models.DateField(_('Due Date'), auto_now_add=False, auto_now=False, null=False, blank=False)
    completed_time = models.DateTimeField(_('rectification completed time'), auto_now_add=False, auto_now=False, null=True, blank=True)


    class Meta:
        verbose_name = _("vehicle inspection")
        verbose_name_plural = _("vehicle inspection")

    def __unicode__(self): 
        return _("vehicle inspection") + " %s %s" % (self.driver.name, self.vehicle.relevant_license_plate)    

    # can be replaced by field.value_to_string(object)
    def my_get_field_display(self,fieldname):

        if not hasattr(self, fieldname):
            return None
        
        field = self._meta.get_field(fieldname)
        return "%s" % self._get_FIELD_display(field)  

    def get_absolute_url(self):
        return reverse("vehicle_inspection_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("vehicle_inspection_update", kwargs={"pk": self.pk })

    def get_absolute_url_list(self):
        return reverse("vehicle_inspection_list", kwargs={})
        
    def is_rectification_qualified(self):
        return self.rectification_qualified == "yes"

    def time_consuming(self):
        return (self.completed_time - self.created).days


class VehicleTransportationKPI(models.Model):
    TRANSPORTATION_PROJECT_OPTION = (
        ('01', _('shuttle bus')),
        ('02', _('general cargo shanghai')),
        ('03', _('general cargo zhejiang')),
        ('04', _('scattered oil (land-and-water coordinated transport)')),        
        ('05', _('Scattered oil (road)')),        
        ('06', _('hazardous article')),        
        ('07', _('water transport')),        
    )

    transportation_project = models.CharField(_("transportation project"), choices=TRANSPORTATION_PROJECT_OPTION, blank=False, null=False, max_length=130)
    year = models.PositiveIntegerField(_("year"),
        validators=[MinValueValidator(2000), MaxValueValidator(timezone.now().year)],
        blank=False,null=False, help_text=_("Use the following format: < YYYY >"))
    month = models.CharField(_("month"),  choices=month_choice, blank=False, null=False,max_length=30)
    safe_mileages = models.PositiveIntegerField(_("safe mileage"), blank=False, null=False)
    safe_labor_hours = models.PositiveIntegerField(_("safe labor hours"), blank=False, null=False)
    LSR_violation_cases = models.PositiveIntegerField(_("LSR violation cases"), blank=False, null=False)
    safety_accident_cases = models.PositiveIntegerField(_("safety accident cases"), blank=False, null=False)
    yearly_plan_executing_rate = PercentageField(_("yearly plan executing rate"), blank=False, null=False,max_length=30)
    vehicle_qualification_rate = PercentageField(_("vehicle qualification rate"), blank=False, null=False,max_length=30)
    journey_management_rules_implemented_rate = PercentageField(_("journey management rules implemented rate"), blank=False, null=False,max_length=30)
    safe_loading_violation_cases = models.PositiveIntegerField(_("safe loading violation cases"), blank=False, null=False)
    departure_count = models.PositiveIntegerField(_("departure count"), blank=False, null=False)
    departure_tones = models.PositiveIntegerField(_("departure tones"), blank=False, null=False)
    monthly_delivery_plan_completion_rate = PercentageField(_("monthly delivery plan completion rate"), blank=False, null=False, max_length=30)
    AOG_on_time_rate = PercentageField(_("AOG on-time rate"), blank=False, null=False,max_length=30)
    POD_on_time_rate = PercentageField(_("POD On-Time rate"), blank=False, null=False,max_length=30)
    POD_accuracy = PercentageField(_("POD accuracy"), blank=False, null=False,max_length=30)
    customer_satisfaction_value = models.DecimalField(_("customer satisfaction rate"), decimal_places=1, max_digits=2, blank=False, null=False)
    customer_complaint_cases = models.PositiveIntegerField(_("Customer complaint cases"), blank=False, null=False)

    class Meta:
        verbose_name = _("vehicle tranportation KPI")
        verbose_name_plural = _("vehicle tranportation KPI")
        unique_together = ('year','month', 'transportation_project')

    def __unicode__(self): 
        return _("vehicle tranportation KPI") + " %s %s %s" % (self.get_transportation_project_display(), self.year, self.get_month_display())     

    # can be replaced by field.value_to_string(object)
    def my_get_field_display(self,fieldname):

        if not hasattr(self, fieldname):
            return None
        
        field = self._meta.get_field(fieldname)
        return "%s" % self._get_FIELD_display(field)       
 

    def get_absolute_url(self):
        return reverse("transportationkpi_detail", kwargs={"pk": self.pk })  

    def get_create_url(self, year, month, project):
        return reverse("transportationkpi_create", kwargs={'year': year, 'month':month, 'project': project })
        
    def get_absolute_url_update(self): 
        return reverse("transportationkpi_update", kwargs={"pk": self.pk })          
