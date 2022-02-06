from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contac_us/', views.contact_us, name='contact_us'),
]