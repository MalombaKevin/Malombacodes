# importations
from . import views
from django.urls import path

# urls setup
urlpatterns=[
    path('', views.index, name='index'),
    path('setup-profile/', views.create_profile, name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('create-post/', views.create_post, name='create_post')
]