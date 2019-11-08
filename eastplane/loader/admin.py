from django.contrib import admin
from .models import *
class getinAdmin(admin.ModelAdmin):
    list_display = ('flight','status','arrtime')
    list_display_links = ('flight',)
    search_fields = ('flight',)
    list_filter = ('status',)
class leftAdmin(admin.ModelAdmin):
    list_display = ('flight', 'status','arrtime')
    list_display_links = ('flight',)
    search_fields = ('flight',)
    list_filter = ('status',)
admin.site.register(tickets)
admin.site.register(ticket)
admin.site.register(getIn,getinAdmin)
admin.site.register(left,leftAdmin)
admin.site.register(user)
# Register your models here.
