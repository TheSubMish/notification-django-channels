from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

@receiver(post_save, sender=Notification)
def store_notification(sender, instance, **kwargs):
    
    channel_layer = get_channel_layer()
    print(instance.receiver.id)
    async_to_sync(channel_layer.group_send)(
        f'notification_{instance.receiver.id}',
        {
            'type': 'send_notification',
            'message': json.dumps({
                'id': instance.id,
                'sender': instance.sender.username,
                'message': instance.message,
                'created_at': instance.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'updated_at': instance.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }),
        }
    )