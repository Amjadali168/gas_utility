from django.urls import path
from .views import submit_request, track_requests

urlpatterns = [
    path('submit/', submit_request, name='submit_request'),
    path('track/', track_requests, name='track_requests'),
]