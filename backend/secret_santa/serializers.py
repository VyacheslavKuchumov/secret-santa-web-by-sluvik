from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, EventParticipant, Wish, Gift, Chat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class EventParticipantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = EventParticipant
        fields = ['id', 'event', 'user', 'joined_at']
        read_only_fields = ['joined_at']


class WishSerializer(serializers.ModelSerializer):
    participant = EventParticipantSerializer(read_only=True)

    class Meta:
        model = Wish
        fields = ['id', 'participant', 'wish_text', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class EventSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    participants = EventParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'event_img',
            'start_date',
            'created_by',
            'description',
            'is_active',
            'participants',
        ]


class GiftSerializer(serializers.ModelSerializer):
    user_from = UserSerializer(read_only=True)
    user_to = UserSerializer(read_only=True)

    class Meta:
        model = Gift
        fields = ['id', 'event', 'user_from', 'user_to']


class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'gift', 'user', 'message', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
