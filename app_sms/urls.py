from django.urls import path, re_path
from . import views


app_name = 'app_sms'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('enviar_sms/', views.enviar_sms, name='enviar_sms'),
 
]
