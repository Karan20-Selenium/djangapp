from django.contrib import admin  
from django.urls import path  
from myapp import views

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('index/', views.index),
    path('info',views.methodinfo),
    path('get',views.getdata),
    path('ssession',views.setsession),
    path('gsession',views.getsession),
    path('scookie',views.setcookie),
    path('gcookie',views.getcookie),
    path('csv',views.getfile),
    path('pdf',views.getpdf),

]     