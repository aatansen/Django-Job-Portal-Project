from django.contrib import admin
from jobApp.models import CustomUserModel,RecruiterProfileModel,SeekerProfileModel,SeekerEducationModel,SeekerWorkExModel,BasicInfoModel,ContactModel,AddJobModel
# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','userType']
admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(RecruiterProfileModel)
admin.site.register(SeekerProfileModel)
admin.site.register(SeekerEducationModel)
admin.site.register(SeekerWorkExModel)
admin.site.register(BasicInfoModel)
admin.site.register(ContactModel)
admin.site.register(AddJobModel)
