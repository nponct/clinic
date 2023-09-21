from django.shortcuts import render
from datetime import datetime,timedelta,date
from rest_framework import viewsets
from django.db.models import Count
from .serializers import ClaimSerializer, DoctorSpecialtySerializer, DoctorSerializer
from . import models
from .models import DoctorSpecialty,Claim


class DoctorSpecialtyView(viewsets.ModelViewSet):
    queryset = DoctorSpecialty.objects.all()
    serializer_class = DoctorSpecialtySerializer

class AllDoctorsView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return models.Doctor.objects.all()

class OnlySpecDoctorsView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return models.Doctor.objects.filter(spec__name=self.kwargs.get('name'))

class OnlySpecClaimView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__spec__name=self.kwargs.get('name'))


class OnlyDoctorClaimView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__lastname=self.kwargs.get('name'))

class AllClaimsOnlySpecNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        return models.Claim.objects.filter(doc__spec__name=self.kwargs.get('name')).\
                annotate(total_count=Count('id'))


class  TodayAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        exsl=date.today().strftime('%Y,%m,%d').split(',')
        return models.Claim.objects.filter(visittime__date=date(int(exsl[0]),int(exsl[1]),int(exsl[2])))


class  TomorrowAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        exs=datetime.today()+timedelta(days=1)
        exsli = exs.strftime('%Y,%m,%d').split(',')
        return models.Claim.objects.filter(visittime__date=date(int(exsli[0]),int(exsli[1]),int(exsli[2])))


class  WeekLaterAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        exs = date.today() + timedelta(days=7)
        exslis = exs.strftime('%Y,%m,%d').split(',')
        return models.Claim.objects.filter(visittime__date=date(int(exslis[0]),int(exslis[1]),
                                                                int(exslis[2])),)

class  OneDoctorWeekLaterAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        exw = date.today() + timedelta(days=7)
        exwlis = exw.strftime('%Y,%m,%d').split(',')
        return models.Claim.objects.filter(doc__lastname=self.kwargs.get('name'),
                                           visittime__date=date(int(exwlis[0]), int(exwlis[1]), int(exwlis[2])))




class  OneDoctorTodayAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        exl = date.today().strftime('%Y,%m,%d').split(',')
        return models.Claim.objects.filter(doc__lastname=self.kwargs.get('name'),
                                          visittime__date=date(int(exl[0]), int(exl[1]), int(exl[2])))


class  OneDoctorTomorrowLaterAllClaimsNumberView(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        extl = datetime.today() + timedelta(days=1)
        extli = extl.strftime('%Y,%m,%d').split(',')
        return models.Claim.objects.filter(doc__lastname=self.kwargs.get('name'),
                                           visittime__date=date(int(extli[0]), int(extli[1]), int(extli[2])))


