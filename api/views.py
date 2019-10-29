from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import ApplicationSerializer, RequestHeaderSerializer, BusinessAddressSerializer, SelfReportedCashFlowSerializer, BusinessSerializer, HomeAddressSerializer, OwnerSerializer, CFApplicationDataSerializer
from .models import *

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


#Application, RequestHeader, BusinessAddress, SelfReportedCashFlow, Business, HomeAddress, Owner, CFApplicationData

# Create your views here.

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()    
    serializer_class = ApplicationSerializer

'''

    @csrf_exempt
    def application_list(self, request):
        """
        List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            application = Application.objects.all()
            serializer = ApplicationSerializer(application, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ApplicationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
'''


class RequestHeaderViewSet(viewsets.ModelViewSet):
    queryset = RequestHeader.objects.all()
    serializer_class = RequestHeaderSerializer

class BusinessAddressViewSet(viewsets.ModelViewSet):
    queryset = BusinessAddress.objects.all()
    serializer_class = BusinessAddressSerializer

class SelfReportedCashFlowViewSet(viewsets.ModelViewSet):
    queryset = SelfReportedCashFlow.objects.all()
    serializer_class = SelfReportedCashFlowSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class HomeAddressViewSet(viewsets.ModelViewSet):
    queryset = HomeAddress.objects.all()
    serializer_class = HomeAddressSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class CFApplicationDataViewSet(viewsets.ModelViewSet):
    queryset = CFApplicationData.objects.all()
    serializer_class = CFApplicationDataSerializer
