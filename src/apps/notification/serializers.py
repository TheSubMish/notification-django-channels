from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    group_id = serializers.CharField(max_length=255, required=True)
    is_read = serializers.HiddenField(default=False)

    class Meta:
        model = Notification
        fields = ['sender', 'group_id', 'message', 'is_read', 'created_at', 'updated_at']

    def create(self, validated_data):
        sender = validated_data.get('sender')
        group_id = validated_data.get('group_id')

        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            raise serializers.ValidationError("Group does not exist")

        if not group.user_set.filter(id=sender.id).exists():
            raise serializers.ValidationError("You are not a member of this group")

        notifications = []
        for user in group.user_set.all():
            notification = Notification(
                sender=sender,
                receiver=user,
                message=validated_data.get('message'),
                is_read=validated_data.get('is_read', False)
            )
            notification.save()
            notifications.append(notification)

        return validated_data
