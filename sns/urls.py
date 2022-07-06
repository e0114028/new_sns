from django.urls import path
from . import views

urlpatterns = [
    path('',views.AcountRegistraion,name='acountregistraion'),
]