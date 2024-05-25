from django.contrib import admin
from .models import Account, Destination
import requests
from django.urls import reverse
from django.conf import settings

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'account_id', 'name', 'app_secret_token', 'website')
    search_fields = ('email', 'name','account_id')
    list_filter = ('name',)


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.destinations.count()>0:
            headers = {
                'Content-Type': 'application/json',
                'CL-X-TOKEN': str(obj.app_secret_token)
            }
            data = {
                'email': obj.email,
                'account_id': obj.account_id,
                'name': obj.name,
                'app_secret_token': str(obj.app_secret_token),
                'website': obj.website,
            }
            
            incoming_data_url = f"{settings.SITE_URL}{reverse('incoming_data')}"
            response = requests.post(incoming_data_url, json=data, headers=headers)
            
            if response.status_code != 200:
                self.message_user(request, f"Failed to call the incoming_data API: {response.content}", level='error')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('account', 'url', 'http_method', 'headers')
    search_fields = ('url', 'http_method')
    list_filter = ('http_method',)
