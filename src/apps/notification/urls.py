from django.urls import path
from .views import CreateNotification,list_notifications

urlpatterns = [
    path('',CreateNotification.as_view(),name='create-notification'),
    path('list',list_notifications,name='list-notifications'),
]