from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
# Create your views here.

class CreateNotification(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Notification created successfully'},status=status.HTTP_201_CREATED)


def list_notifications(request, *args, **kwargs):
    notifications = Notification.objects.filter(receiver=request.user)
    user_id = request.user.id
    return render(request, 'index.html', {'notifications': notifications,'user_id':user_id})