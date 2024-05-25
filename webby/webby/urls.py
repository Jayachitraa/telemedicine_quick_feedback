from django.urls import path, include
from rest_framework.routers import DefaultRouter
from webhookify.views import AccountViewSet, DestinationViewSet, get_destinations, incoming_data

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/<int:account_id>/destinations/', get_destinations, name='get_destinations'),
    path('server/incoming_data/', incoming_data, name='incoming_data'),
]
