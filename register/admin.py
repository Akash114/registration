from django.contrib import admin
from .models import Registration,Reservation
from django.contrib.auth.models import Group,User
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.site_header = "Grise Admin"
admin.site.site_title = "Grise Registration Admin Area"
admin.site.index_title = "Welcome to the Grise Registration Admin Area"


class RegistrationInfoAdmin(admin.ModelAdmin):
    list_display = ('bsc_address','nami_address','register_date')


class ReservationResource(resources.ModelResource):
    class Meta:
        model = Reservation
        fields = ('slot_number', 'address', 'amount','amount_BNB',)


class ReservationAdmin(ImportExportModelAdmin):
    resource_class = ReservationResource
    list_display = ('slot_number', 'address', 'amount','amount_BNB',)


admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Registration,RegistrationInfoAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
