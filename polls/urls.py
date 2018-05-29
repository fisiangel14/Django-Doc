from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='inicio')
]

#2.Lego creo una url en mi app