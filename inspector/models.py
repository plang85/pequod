from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import django.utils.timezone as future_time_requested
# Create your models here.


class Request(models.Model):
    requested = models.DateTimeField('date requested', default=future_time_requested.now)
    url_rpt = models.CharField(max_length=200, blank=True, default='')
    base64_audio = models.TextField(blank=True, default='')


    class Meta:
        ordering = ('requested',)


class Response(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    response = models.CharField(max_length=200, blank=True, default='')
    transcript = models.CharField(max_length=200, blank=True, default='')


    class Meta:
        ordering = ('request',)