from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Event, EventParticipant, Wish, Gift, Chat


class EventParticipantInline(admin.TabularInline):
    model = EventParticipant
    extra = 0
    readonly_fields = ('user', 'joined_at')
    can_delete = True
    show_change_link = True


class GiftInline(admin.TabularInline):
    model = Gift
    extra = 0
    readonly_fields = ('user_from', 'user_to')
    can_delete = True
    show_change_link = True


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'start_date', 'created_by', 'is_active')
    list_filter = ('is_active', 'start_date', 'created_by')
    search_fields = ('event_name', 'description', 'created_by__username')
    inlines = [EventParticipantInline, GiftInline]
    readonly_fields = ('created_by',)
    fieldsets = (
        (None, {
            'fields': ('event_name', 'event_img', 'description', 'start_date', 'is_active', 'created_by')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


@admin.register(EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'joined_at')
    list_filter = ('event', 'joined_at')
    search_fields = ('event__event_name', 'user__username')
    readonly_fields = ('joined_at',)


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('participant', 'wish_text', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('participant__user__username', 'wish_text')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('event', 'user_from', 'user_to')
    list_filter = ('event',)
    search_fields = ('event__event_name', 'user_from__username', 'user_to__username')
    inlines = []
    readonly_fields = ()


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('gift', 'user', 'message', 'created_at', 'updated_at')
    list_filter = ('created_at', 'gift', 'user')
    search_fields = ('message', 'gift__event__event_name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
