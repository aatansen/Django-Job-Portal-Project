from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobProject.views import signup,signin,dashboard,logoutpage,profile,profileinfo,recruiterprofile,seekerprofile,seekereducation,seekerworkex,basicinfo,contactinfo,editprofile,addjob,viewalljob,deletejob,editjob,viewsinglejob,changepassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('profile/',profile,name='profile'),
    path('profileinfo/',profileinfo,name='profileinfo'),
    path('recruiterprofile/',recruiterprofile,name='recruiterprofile'),
    path('seekerprofile/',seekerprofile,name='seekerprofile'),
    path('seekereducation/',seekereducation,name='seekereducation'),
    path('seekerworkex/',seekerworkex,name='seekerworkex'),
    path('basicinfo/',basicinfo,name='basicinfo'),
    path('contactinfo/',contactinfo,name='contactinfo'),
    path('editprofile/',editprofile,name='editprofile'),
    path('addjob/',addjob,name='addjob'),
    path('viewalljob/',viewalljob,name='viewalljob'),
    path('deletejob/<str:jobid>',deletejob,name='deletejob'),
    path('editjob/<str:jobid>',editjob,name='editjob'),
    path('viewsinglejob/<str:jobid>',viewsinglejob,name='viewsinglejob'),
    path('changepassword/',changepassword,name='changepassword'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
