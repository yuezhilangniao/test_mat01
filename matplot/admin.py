from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PartInfo,ManInfo

class PartInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
class ManInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','yeji','huikuan','hetong']

admin.site.register(PartInfo,PartInfoAdmin)
admin.site.register(ManInfo,ManInfoAdmin)