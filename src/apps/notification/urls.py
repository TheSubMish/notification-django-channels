from django.urls import path
from .views import CreateNotification

urlpatterns = [
    path('',CreateNotification.as_view(),name='create-notification'),
]