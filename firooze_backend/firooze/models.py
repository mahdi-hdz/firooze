from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User


class Residents(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    number = models.CharField(max_length=18, null=False, blank=True)
    block = models.CharField(max_length=4, null=False, blank=False)
    floor = models.CharField(max_length=2, null=False, blank=False)     # طبقه
    unit = models.CharField(max_length=2, null=False, blank=False)     # واحد
    debt = models.CharField(max_length=10)      # بدهی


class Message(models.Model):
    senderName = models.CharField(max_length=50, null=False, blank=False)
    senderEmail = models.EmailField()
    message = models.TextField()
    send_at = models.DateTimeField(default=timezone.now)


class Notif(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    content = RichTextField()
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)


    @property
    def short_content(self):
        return truncatechars(self.content, 200)
