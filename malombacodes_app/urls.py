# importations
from . import views
from django.urls import path

# urls setup
urlpatterns=[
    path('', views.index, name='index')
]