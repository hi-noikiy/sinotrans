from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class TrainingCourse(models.Model):

    TRAINING_CATEGORY_OPTION = (
        ('work license',_('work license')),
        ('annual training plan',_('annual training plan')),
        ('meeting before work',_('meeting before work')),
        ('other',_('other')),
    )

    date = models.DateField(_('training date'), auto_now_add=False, auto_now=False)
    location = models.CharField(_('training location'),max_length=30, blank=False, null=False)
    topic = models.CharField(_('training topic'), max_length=150, blank=False, null=False)
    category = models.CharField(_('training category'), choices=TRAINING_CATEGORY_OPTION, max_length=150, blank=False, null=False)
    content = models.TextField(_('training content'),blank=True, null=True)

    class Meta:
        verbose_name = _("training course")
        verbose_name_plural = _("training courses")

    def __unicode__(self): 
        return _("training course") + self.topic

class AnnualTraningPlan(models.Model):
    training_course = models.ForeignKey(TrainingCourse, verbose_name=_("training"))
    planned_date = models.DateField(_('planned date'), auto_now_add=False, auto_now=False)
    actual_date = models.DateField(_('actual date'), auto_now_add=False, auto_now=False, blank=True, null=True)

    class Meta:
        verbose_name = _("annual training plan")
        verbose_name_plural = _("annual training plan")

    def __unicode__(self): 
        return _("annual training plan") + self.training_course.topic

class TrainingPerson(models.Model):
    POSITION_OPTION = (
        ('driver',_('driver')),
        ('forklift driver',_('forklift driver')),
        ('project manager',_('project manager')),
    )

    training_course = models.ForeignKey(TrainingCourse, verbose_name=_("training"))
    trainee = models.CharField(_("trainee"), max_length=30,  blank=False, null=False)
    score = models.PositiveIntegerField(_("score"), blank=False, null=False)
    work_position = models.CharField(_("work position"), max_length=30, choices=POSITION_OPTION, blank=False, null=False)

    class Meta:
        verbose_name = _("training person")
        verbose_name_plural = _("training persons")

    def __unicode__(self): 
        return _("training person") + self.trainee    