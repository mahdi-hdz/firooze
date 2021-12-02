from django.contrib import admin
from .models import *
# Register your models here.


class ResidentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'debt', 'block', 'floor',  'unit', 'number']


admin.site.register(Residents, ResidentsAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ['senderName', 'senderEmail', 'message']


admin.site.register(Message, MessageAdmin)


class NotifAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'short_content', 'created_at']


admin.site.register(Notif, NotifAdmin)




