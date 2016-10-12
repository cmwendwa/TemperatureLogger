from django.db import models
from django.utils.translation import gettext as _
# Create your models here.



class TemperatureLog(models.Model):
    timestamp = models.DateTimeField(_("timestamp"),)
    temperature = temperature = models.IntegerField(_("temperature (C°)"),)
    
    class Meta:
        verbose_name=_("temperature log")
        verbose_name_plural=_("temperature logs")
        ordering = ("-timestamp",)




    def __str__(self):
        return "@ %s" % (
            self.timestamp.strftime("%Y-%m-%dT%H:%M"),
            )



