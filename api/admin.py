from django.contrib import admin
from .models import Application, RequestHeader, BusinessAddress, SelfReportedCashFlow, Business, HomeAddress, Owner, CFApplicationData
# Register your models here.

admin.site.register(Application)
admin.site.register(RequestHeader)
admin.site.register(BusinessAddress)
admin.site.register(Business)
admin.site.register(SelfReportedCashFlow)
admin.site.register(HomeAddress)
admin.site.register(Owner)
admin.site.register(CFApplicationData)