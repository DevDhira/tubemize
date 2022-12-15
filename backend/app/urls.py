from django.urls import path,include
from .views import add_channel, check_channel, return_details

urlpatterns = [    
    path('add-channel/', add_channel, name='add-channel'),    
    path('check-status/', check_channel, name='check-status'),    
    path('stats/', return_details, name='stats'),    
]