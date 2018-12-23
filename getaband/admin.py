from django.contrib import admin

from .models import UserProfile,Instruments,urls

admin.site.register(UserProfile)
admin.site.register(Instruments)
admin.site.register(urls)