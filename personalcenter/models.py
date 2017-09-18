
from django.db import models
from django.conf import settings
# Create your models here.


    

class UserProfile(models.Model): 
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    score = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    # score_available = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    # score_frozen = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    # score_owned = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    # score_spent = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    level = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __unicode__(self):  
        return str(self.user)
