import stripe
import json

from django.conf import settings
from django.shortcuts import redirect


from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import CustomerPayment
from accounts.models import EmailUser

FRONTEND_SUBSCRIPTION_SUCCESS_URL = settings.SUBSCRIPTION_SUCCESS_URL
FRONTEND_SUBSCRIPTION_CANCEL_URL = settings.SUBSCRIPTION_FAILED_URL

webhook_secret = settings.STRIPE_WEBHOOK_SECRET
stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request):
    try:

        price_id = ''

        if request.data['plan'] == 'basic':
            price_id = 'price_1LD7XcKPyJLjGRo4peZvp8ed'

        if request.data['plan'] == 'premium':
            price_id = 'price_1LD7Y5KPyJLjGRo4B150gCta'

        

        if CustomerPayment.objects.filter(customer=request.user).exists():
            return Response(status=status.HTTP_409_CONFLICT, data={"detail": "You Already have a subscription , First Cancel that then Subscribe to New one!"})
        else:
            checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1
                }
            ],
            mode='subscription',
            success_url=FRONTEND_SUBSCRIPTION_SUCCESS_URL +
            "/{CHECKOUT_SESSION_ID}",
            cancel_url=FRONTEND_SUBSCRIPTION_CANCEL_URL,
            customer_email=request.user.email
        
        )

       # return redirect(checkout_session.url, code=303)
        return Response({"url":checkout_session.url})
    except Exception as err:
        raise err


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_customer(request):
    session_id = request.data['session_id']
    session = stripe.checkout.Session.retrieve(session_id)

    customer = stripe.Customer.retrieve(session.customer)

    subscription_details = stripe.Subscription.list(customer=customer)

    subscriptionid = subscription_details.data[0].id
    customerid = subscription_details.data[0].customer
    priceid = subscription_details.data[0].plan.id
    productid = subscription_details.data[0].plan.product

    res = {
        "subscriptionid": subscriptionid,
        "customerid": customerid,
        "priceid" : priceid,
        "productid": productid
    }

    customer_payment = CustomerPayment()
    customer_user = EmailUser.objects.get(email=request.user.email)

    customer_payment.customer = customer_user
    customer_payment.subscriptionid = subscriptionid
    customer_payment.customerid = customerid
    customer_payment.priceid = priceid
    customer_payment.productid = productid

    customer_payment.save()




    return Response(json.dumps(res))


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def cancel_subscription(request):

    customer_payment = CustomerPayment.objects.get(customer=request.user)

    subscription_id = customer_payment.subscriptionid


    stripe.Subscription.delete(subscription_id)

    customer_payment.delete()

    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def get_payment_status(request):
    plan = ''
    try:
        customer_payment = CustomerPayment.objects.get(customer=request.user)

        if customer_payment.priceid == 'price_1LD7XcKPyJLjGRo4peZvp8ed':
            plan = 'basic'
    
        if customer_payment.priceid == 'price_1LD7Y5KPyJLjGRo4B150gCta':
            plan = 'premium'
    
    except Exception as e :
       plan = 'free'
          


    
    return Response({"plan":plan})

    

        