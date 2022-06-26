# importations
from django.conf import settings
from django.urls import path
from django import views
from . import views
from django.conf.urls.static import static

# urls setup
urlpatterns=[
    path('', views.index, name='index'),
    path('setup-profile/', views.create_profile, name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('create-post/', views.create_post, name='create_post'),
    path('create-meme/', views.create_meme, name='create_meme'),
    path('memes/', views.memes, name='memes'),
    path('malombacoders/', views.all_users, name='malombacoders'),
    path('malombacoder/<int:id>', views.user, name='malombacoder'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)