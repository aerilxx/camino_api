from rest_framework import serializers
from .models import Application, RequestHeader, BusinessAddress, SelfReportedCashFlow, Business, HomeAddress, Owner, CFApplicationData

class RequestHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestHeader
        fields = ['CFRequestId', 'RequestDate', 'CFApiUserId', 'CFApiPassword','IsTestLead']

class BusinessAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAddress
        fields = ['Address1', 'Address2', 'City', 'State','Zip']

class SelfReportedCashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfReportedCashFlow
        fields = ['AnnualRevenue', 'MonthlyAverageBankBalance', 'MonthlyAverageCreditCardVolume']

class BusinessSerializer(serializers.ModelSerializer):
    SelfReportedCashFlow = SelfReportedCashFlowSerializer
    BusinessAddress = BusinessAddressSerializer
    class Meta:
        model = Business
        fields = ['Name', 'SelfReportedCashFlow', 'Address', 'TaxID','Phone','NAICS','HasBeenProfitable','HasBankruptedInLast7Years','InceptionDate']
        depth = 2

class HomeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAddress
        fields = ['Address1', 'City', 'State','Zip']

class OwnerSerializer(serializers.ModelSerializer):
    HomeAddress = HomeAddressSerializer
    class Meta:
        model = Owner
        fields = ['Name', 'FirstName', 'LastName','Email','HomeAddress','DateOfBirth','HomePhone','SSN','PercentageOfOwnership']
        depth = 2

class CFApplicationDataSerializer(serializers.ModelSerializer):
     class Meta:
        model = CFApplicationData
        fields = ['RequestedLoanAmount', 'StatedCreditHistory', 'LegalEntityType','FilterID']

class ApplicationSerializer(serializers.ModelSerializer):
    RequestHeader = RequestHeaderSerializer
    Business = BusinessAddressSerializer
    Owner = OwnerSerializer
    CFApplicationData = CFApplicationDataSerializer

    class Meta:
        model = Application
        fields = ['RequestHeader','Business','Owner', 'CFApplicationData' ]
        depth = 3

    '''
    def create(self, validated_data):
        print(validated_data)
        requestHeader = validated_data.pop('RequestHeader')
        business = validated_data.pop('Business')
        owner = validated_data.pop('Owner')
        cFApplicationData = validated_data.pop('CFApplicationData')

        application = Application.objects.create(**validated_data)

        RequestHeader.objects.create(Application=application, **requestHeader)
        Business.objects.create(Application=application, **business)
        Owner.objects.create(Application=application, **owner)
        CFApplicationData.objects.create(Application=application, **cFApplicationData)
        return application
    '''
