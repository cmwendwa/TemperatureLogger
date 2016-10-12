from django.db import models
from django import template
from django.template import loader
from core.models import TemperatureLog

register = template.Library()



@register.simple_tag
def get_temperature_times():
    time=list()
    temperature_logs = TemperatureLog.objects.all().order_by('timestamp')
    for item in temperature_logs:
        temp = int(item.timestamp.strftime("%Y%m%d"))
        time.append(temp)
    return time
@register.simple_tag
def get_temperature_values():
    values =list()
    temperature_logs =TemperatureLog.objects.all().order_by('timestamp')
    for item in temperature_logs:
        values.append(item.temperature)
    return values


@register.simple_tag
def get_min_temperature_value():
    values =list()
    temperature_logs =TemperatureLog.objects.all().order_by('timestamp')
    for item in temperature_logs:
        values.append(item.temperature)
    return min(values)-10
