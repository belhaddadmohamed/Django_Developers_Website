from django.contrib import admin
from .models import Profile, Skill, Message


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'short_intro', 'location']



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill)
admin.site.register(Message)