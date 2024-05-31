"""
URL configuration for gympro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('team/',views.team,name='team'),
    path('about/',views.about,name='about'),
    path('feedback/',views.feedback,name='feedback'),
    path('class/',views.clas,name='class'),
    path('contact/',views.contact,name='contact'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    #####
    path('view/',views.view),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delet/<int:id>',views.delet),
    path('logout/',views.logout),
    path('adminlogout/',views.adminlogout),
    path('employees/',views.employees),
    path('addnewemployee/',views.addnewemployee),
    path('empedit/<int:id>',views.empedit),
    path('empupdate/<int:id>',views.empupdate),
    path('empdelet/<int:id>',views.empdelet),
    path('feedbackpage/',views.feedbackpage),
    path('feedbackdelet/<int:id>',views.feedbackdelet),
    path('empaccount/',views.empaccount),
    path('accounts/',views.accounts),
    path('customeraccount/',views.customeraccount),
    path('useraccount/',views.useraccount),
    path('editempaccount/<int:id>',views.editempaccount),
    path('empaccountupdate/<int:id>',views.empaccountupdate),
    path('deletempaccount/<int:id>',views.deletempaccount),
    path('editcustomeraccount/<int:id>',views.editcustomeraccount),
    path('customeraccountupdate/<int:id>',views.customeraccountupdate),
    path('deletecustomeraccount/<int:id>',views.deletecustomeraccount)
    
    
    
    
]
