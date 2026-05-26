from django.contrib import admin
from .models import CompatibilityScore, Message


@admin.register(CompatibilityScore)
class CompatibilityScoreAdmin(admin.ModelAdmin):
    list_display = ['from_profile', 'to_profile', 'score', 'calculated_at']
    ordering = ['-score']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'sent_at', 'read_at']
    ordering = ['-sent_at']