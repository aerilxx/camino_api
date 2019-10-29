from django.db import models

class RequestHeader(models.Model):
    CFRequestId = models.IntegerField()
    RequestDate = models.DateTimeField(auto_now_add = True)
    CFApiUserId = models.CharField(max_length=60, blank=True, null=False)
    CFApiPassword = models.CharField(max_length=60, blank=True, null=False)
    IsTestLead = models.BooleanField()

class BusinessAddress(models.Model):
    Address1 = models.CharField(max_length=250)
    Address2 = models.CharField(max_length=250, null = True)
    City = models.CharField(max_length=25)
    State = models.CharField(max_length=3)
    Zip = models.IntegerField()

class SelfReportedCashFlow(models.Model):
    AnnualRevenue = models.DecimalField(max_digits=8, decimal_places=2)
    MonthlyAverageBankBalance = models.DecimalField(max_digits=8, decimal_places=2)
    MonthlyAverageCreditCardVolume = models.DecimalField(max_digits=8, decimal_places=2)

class Business(models.Model):
    Name = models.CharField(max_length=250)
    SelfReportedCashFlow = models.ForeignKey(SelfReportedCashFlow, on_delete=models.CASCADE)
    Address = models.ForeignKey(BusinessAddress, on_delete=models.CASCADE)
    TaxID = models.IntegerField()
    Phone = models.CharField(max_length=12)
    NAICS = models.IntegerField(primary_key=True)
    HasBeenProfitable = models.BooleanField()
    HasBankruptedInLast7Years = models.BooleanField()
    InceptionDate = models.DateTimeField(auto_now_add = True)

class HomeAddress(models.Model):
    Address = models.CharField(max_length=250)
    City = models.CharField(max_length=25)
    State = models.CharField(max_length=10)
    Zip = models.IntegerField()

class Owner(models.Model):
    Name = models.CharField(max_length=120)
    FirstName = models.CharField(max_length=120)
    LastName = models.CharField(max_length=120)
    Email = models.EmailField()
    HomeAddress = models.ForeignKey(HomeAddress, on_delete=models.CASCADE)
    DateOfBirth = models.DateField()
    HomePhone = models.CharField(max_length=12)
    SSN = models.CharField(max_length = 10, primary_key=True)
    PercentageOfOwnership = models.FloatField()


class CFApplicationData(models.Model):
     RequestedLoanAmount = models.DecimalField(max_digits=8, decimal_places=2)
     StatedCreditHistory = models.IntegerField()
     LegalEntityType = models.CharField(max_length=5)
     FilterID = models.IntegerField(null=True)


class Application(models.Model):
    RequestHeader = models.ForeignKey(RequestHeader,null=True, on_delete=models.CASCADE)
    Business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    Owner = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)
    CFApplicationData = models.ForeignKey(CFApplicationData, null=True, on_delete=models.CASCADE)

   