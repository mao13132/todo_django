from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_works, name='list_works'),

]
