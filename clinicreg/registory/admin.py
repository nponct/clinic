from django.contrib import admin

from .import models






@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=('spec','lastname',)
    list_display_links=('lastname',)

@admin.register(models.DoctorSpecialty)
class DoctorSpecialtyAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_display_links=('name',)



@admin.register(models.Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display=('nickname','doc','problem_description','visittime',)
    filter_horizontal = ('otherdocs',)
    list_display_links=('nickname',)

