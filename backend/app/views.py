import json
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import TubeDetails
from payment.models import CustomerPayment

from datetime import datetime, date

from .overall_score import overall_score

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def add_channel(request):   
    if request.data['channel_id'] :
        if not TubeDetails.objects.filter(user = request.user).exists():
            tube_details = TubeDetails()
            tube_details.channelid = request.data['channel_id']
            tube_details.user = request.user
            tube_details.date = datetime.now()
            tube_details.save()
            return Response("Channel Added")

        else:
            return Response(status=status.HTTP_409_CONFLICT,data={"message":"User with channel Already Exists"})
    else:
        return Response("Please Provide the Channel Id")

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def check_channel(request):

    if TubeDetails.objects.filter(user = request.user).exists():
            return Response(status=status.HTTP_200_OK,data={"message":"true"})
    else:
        return Response(status=status.HTTP_200_OK,data={"message":"false"})

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def return_details(request):
    if TubeDetails.objects.filter(user = request.user).exists():
        tube_details = TubeDetails.objects.get(user = request.user)
        try:
            paid_customer = CustomerPayment.objects.get(customer= request.user)
            user_plan = paid_customer.priceid 
        except Exception as e:
            user_plan='free'
        
        if user_plan == 'free':
            limit = 1

        if user_plan == 'price_1LD7XcKPyJLjGRo4peZvp8ed':
            limit = 2

        if user_plan == 'price_1LD7Y5KPyJLjGRo4B150gCta':
            limit = 3

        if date.today() == tube_details.date:

            if tube_details.count < limit:
                percentage = overall_score(tube_details.channelid)
                tube_details.count = tube_details.count + 1
                tube_details.save()

                return Response({json.dumps(percentage)})

            else:
                return Response({"message":"You exceeded your limits"})
        else:
            tube_details.count = 0
            tube_details.date  = datetime.today()
            tube_details.save()
            tube_details = TubeDetails.objects.get(user = request.user)

            if tube_details.count < limit:
                percentage = overall_score(tube_details.channelid)
                tube_details.count = tube_details.count + 1
                tube_details.save()

                return Response({ percentage})

            else:
                return Response({"message":"You exceeded your limits"})
    else:
        return Response({"message":"User not exists"})
            
        


        

