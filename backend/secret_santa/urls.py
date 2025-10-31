from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EventViewSet,
    EventParticipantViewSet,
    WishViewSet,
    GiftViewSet,
    ChatViewSet,
)

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'participants', EventParticipantViewSet)
router.register(r'wishes', WishViewSet)
router.register(r'gifts', GiftViewSet)
router.register(r'chats', ChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
