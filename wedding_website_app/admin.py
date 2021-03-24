from django.contrib import admin
from .models import Guest

class GuestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_shu_friend_relative', 'is_peggy_friend_relative','number_of_guests', 'diet_restriction')
    search_fields = ('diet_restriction',)

admin.site.register(Guest, GuestAdmin)