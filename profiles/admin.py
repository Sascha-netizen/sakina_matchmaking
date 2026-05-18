from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'country', 'sect', 'completed', 'created_at')
    list_filter = ('gender', 'sect', 'marital_status', 'completed', 'profile_visibility')
    search_fields = ('user__username', 'country', 'city', 'ethnicity')

