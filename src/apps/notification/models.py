from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Notification Sender",
        related_name='sent_notifications'
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
        verbose_name="Notification Receiver",
        related_name='received_notifications'
    )
    message = models.CharField(
        max_length=255,
        verbose_name="Notification Message"
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="Notification Read Status"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Notification Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Notification Updated At"
    )

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f'{self.sender} sent notification to {self.receiver}'