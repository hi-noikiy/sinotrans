from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete, post_save, pre_save
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class TrainingCourse(models.Model):

    TRAINING_CATEGORY_OPTION = (
        ('work license',_('work license')),
        ('annual training plan',_('annual training plan')),
        ('meeting before work',_('meeting before work')),
        ('other',_('other')),
    )

    TRAINING_CLASS_OPTION = (
        ('warehouse',_('warehouse')),
        ('transportation',_('transportation')),
    )


    training_class = models.CharField(_('training class'), choices=TRAINING_CLASS_OPTION, max_length=150, default='warehouse',blank=False, null=False)
    topic = models.CharField(_('training topic'), max_length=150, blank=False, null=False)
    category = models.CharField(_('training category'), choices=TRAINING_CATEGORY_OPTION, max_length=150, blank=False, null=False)
    content = RichTextField(_('training content'),blank=True, null=True)

    class Meta:
        verbose_name = _("training course")
        verbose_name_plural = _("training courses")

    def __unicode__(self): 
        return self.topic
        # return _("training course") + self.topic

    def get_absolute_url(self):
        print self.pk
        return reverse("trainingcourse_detail", kwargs={"pk": self.pk })

class TrainingRecord(models.Model):

    training_course = models.ForeignKey(TrainingCourse, verbose_name=_("training course"))
    date = models.DateField(_('training date'), auto_now_add=False, auto_now=False)
    location = models.CharField(_('training location'),max_length=30, blank=False, null=False)    
    trainer = models.CharField(_("trainer"), max_length=30,  blank=False, null=False)
    audiences = models.CharField(_("audiences"), max_length=30,  blank=False, null=False)

    class Meta:
        verbose_name = _("training record")
        verbose_name_plural = _("training record")

    def __unicode__(self): 
        #return _("training record") + " %s %s" % (self.training_course.topic , self.date )
        return" %s %s" % (self.training_course.topic , self.date )

    def get_absolute_url(self):
        return reverse("trainingrecord_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("trainingrecord_update", kwargs={"pk": self.pk })
        
class TrainingTranscript(models.Model):
    POSITION_OPTION = (
        ('driver',_('driver')),
        ('forklift driver',_('forklift driver')),
        ('project manager',_('project manager')),
    )

    training_record = models.ForeignKey(TrainingRecord, verbose_name=_("training record"))
    trainee = models.CharField(_("trainee"), max_length=30,  blank=False, null=False)
    score = models.PositiveIntegerField(_("score"), blank=False, null=False)
    work_position = models.CharField(_("work position"), max_length=30, choices=POSITION_OPTION, blank=False, null=False)

    class Meta:
        verbose_name = _("training transcript")
        verbose_name_plural = _("training transcript")

    def __unicode__(self): 
        return _("training transcript") + self.trainee    

    def get_absolute_url(self):
        return reverse("trainingtranscript_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("trainingtranscript_update", kwargs={"pk": self.pk })


class AnnualTraningPlan(models.Model):
    year = models.PositiveIntegerField(_("year"),
        validators=[MinValueValidator(2000), MaxValueValidator(timezone.now().year)],
        blank=False,null=False, help_text=_("Use the following format: < YYYY >"))    
    training_course = models.ForeignKey(TrainingCourse, verbose_name=_("training"))
    planned_date = models.DateField(_('planned date'), auto_now_add=False, auto_now=False)
    actual_date = models.DateField(_('actual date'), auto_now_add=False, auto_now=False, blank=True, null=True)
    training_record = models.OneToOneField(TrainingRecord, verbose_name=_("training record"), blank=True, null=True)

    class Meta:
        verbose_name = _("annual training plan")
        verbose_name_plural = _("annual training plan")

    def __unicode__(self): 
        return _("annual training plan") + " %s %s" % (self.training_course.topic, self.planned_date)        

    def get_absolute_url(self):
        return reverse("annualtrainingplan_detail", kwargs={"pk": self.pk })

    def get_absolute_url_update(self):
        return reverse("annualtrainingplan_update", kwargs={"pk": self.pk })
        
def update_actual_date(sender, instance, *args, **kwargs):

    if instance.training_record and instance.training_record.date and not instance.actual_date:
        instance.actual_date = instance.training_record.date
        instance.save()

post_save.connect(update_actual_date, sender=AnnualTraningPlan)        
