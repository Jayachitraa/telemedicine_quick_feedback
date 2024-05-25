from django.contrib import admin
from .models import Account, Destination

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'account_id', 'name', 'app_secret_token', 'website')
    search_fields = ('email', 'name','account_id')
    list_filter = ('name',)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('account', 'url', 'http_method', 'headers')
    search_fields = ('url', 'http_method')
    list_filter = ('http_method',)
