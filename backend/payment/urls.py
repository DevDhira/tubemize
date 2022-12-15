from django.urls import path,include
from .views import create_payment, save_customer,cancel_subscription,get_payment_status

urlpatterns = [    
    path('checkout/', create_payment, name='create_payment'),    
    path('session/', save_customer, name='save_customer'),
    path('cancel/', cancel_subscription, name='cancel_subscription'),
    path('status/', get_payment_status, name='get_payment_status'),
        
]