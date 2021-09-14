from django.contrib import admin
from django.urls import path,include 
from . import views 
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/<int:id>',views.profile,name = 'profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path(r'^comment/(?P<image_id>\d+)', views.comment,name = "comment"),
    path('upload/image', views.upload_image, name = "upload_image"),
    path(r'^like/(?P<image_id>\d+)', views.like_photo, name = 'like_photo'),
    path(r'^search/', views.search_users, name='search_users')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
