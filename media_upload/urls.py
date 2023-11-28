# urls.py in your app

from django.urls import path
from .views import upload_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    # Add other URL patterns as needed
]
