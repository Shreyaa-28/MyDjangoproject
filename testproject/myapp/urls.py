from django.urls import path
from . import views

urlpatterns = [ 
                path("",views.homepageview),
                path("Home",views.homepageview),
                path("about",views.aboutpage),
                path("contact",views.contactpage),
                path("form",views.formpageview),
                path("process",views.formpageprocess),
                path("add-Student",views.addStudent),
                path("display-student",views.displayStudent),
                ]