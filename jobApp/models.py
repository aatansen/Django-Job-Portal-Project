from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    profilePhoto = models.ImageField(upload_to='static/user_profile')
    age=models.CharField(max_length=100)
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    gender=models.CharField(choices=GENDER,max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    bloodGroup=models.CharField(max_length=100)
    USER_TYPE=[
        ('seeker','Job Seeker'),
        ('recruiter','Job Recruiter'),
    ]
    userType = models.CharField(choices=USER_TYPE,max_length=100)
    
    def __str__(self):
        return self.username

# Recruiter models:
class RecruiterProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruiterprofilemodel')
    Company_name=models.CharField(max_length=100)
    Company_location=models.CharField(max_length=100)
    Recruiter_Name=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

# Seeker models:
class SeekerProfileModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekerprofilemodel')
    Qualification=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Skills=models.CharField(max_length=100)
    LAST_EDUCATION=[
        ('jsc','JSC'),
        ('ssc','SSC'),
        ('hsc','HSC'),
    ]
    last_education = models.CharField(choices=LAST_EDUCATION,max_length=100)

    def __str__(self):
        return self.user.username

class SeekerEducationModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekereducationmodel')
    education_name=models.CharField(max_length=100)
    education_year=models.CharField(max_length=100)
    education_institute=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class SeekerWorkExModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='seekerworkexmodel')
    Position=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)
    Duration=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# Common models 
class BasicInfoModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='basicinfomodel')
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class ContactModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='contactmodel')
    mobile_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class AddJobModel(models.Model):
    created_by = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    company_description = models.TextField()
    job_description = models.TextField()
    qualification = models.CharField(max_length=100)
    salary_information = models.CharField(max_length=100)
    deadline = models.DateField()
    designation = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    
    def __str__(self):
        return self.created_by.username