from django.urls import path
from .templates import mamboView, mamboBacklog

urlpatterns = [
    path('mambo/', mamboView, name='mambo'),
    path('backlog/', mamboBacklog, name='backlog')
]