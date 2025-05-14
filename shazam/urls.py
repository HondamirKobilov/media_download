from django.urls import path
from . import views
from .views import fetch_instagram_media

app_name = "shazam"

urlpatterns = [
    path('', views.index, name='index'),  # http://localhost:8000/shazam/
    path('api/fetch_instagram_media/', fetch_instagram_media, name='fetch_instagram_media'),
]
