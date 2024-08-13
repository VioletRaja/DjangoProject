from django.urls import path
from .import views
from DjangoProject import urls

urlpatterns=[
    path('',views.index,name="index"),
    path('service',views.service,name="service"),
    path('projects',views.projects,name="projects"),
    path('contact',views.contact,name="contact"),
    path('contact/addrec',views.addrec,name="addrec"),
    path('contact/addrec_home',views.addrec_home,name="addrec_home"),    
]






    

