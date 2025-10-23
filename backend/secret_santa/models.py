from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_img = models.ImageField(upload_to='events/', null=True, blank=True)
    start_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')

class Wish(models.Model):
    participant = models.OneToOneField(EventParticipant, on_delete=models.CASCADE, related_name='wish')
    wish_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gift(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='gifts')
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gifts_given')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gifts_received')

    class Meta:
        unique_together = ('event', 'user_from')

class Chat(models.Model):
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
