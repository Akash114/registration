from django.contrib import admin
from .models import Registration
from django.contrib.auth.models import Group,User

# Register your models here.

admin.site.site_header = "Grise Admin"
admin.site.site_title = "Grise Registration Admin Area"
admin.site.index_title = "Welcome to the Grise Registration Admin Area"


class RegistrationInfoAdmin(admin.ModelAdmin):
    list_display = ('bsc_address','nami_address','register_date')


admin.site.register(Registration,RegistrationInfoAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
