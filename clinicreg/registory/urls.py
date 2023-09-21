from .import views
from django.urls import path



urlpatterns=[

    path('doctors/',views.AllDoctorsView.as_view({'get':'list','post':'create'})),
    path('doctor/<str:name>/',views.OnlySpecDoctorsView.as_view({'get':'list','post':'create'})),
    path('claims/<str:name>/',views.OnlySpecClaimView.as_view({'get':'list','post':'create'})),
    path('claim/<str:name>/',views.OnlyDoctorClaimView.as_view({'get':'list','post':'create'})),
    path('claimsnumber/<str:name>/',views.AllClaimsOnlySpecNumberView.as_view({'get':'list','post':'create'})),
    path('todclaimsnumber/',views.TodayAllClaimsNumberView.as_view({'get':'list','post':'create'})),
    path('tomclaimsnumber/',views.TomorrowAllClaimsNumberView.as_view({'get':'list','post':'create'})),
    path('weekclaimsnumber/',views.WeekLaterAllClaimsNumberView.as_view({'get':'list','post':'create'})),
    path('todclaimnumber/<str:name>/',views.OneDoctorTodayAllClaimsNumberView.as_view({'get':'list','post':'create'})),
    path('tomclaimnumber/<str:name>/',views.OneDoctorTomorrowLaterAllClaimsNumberView.as_view({'get':'list','post':'create'})),
    path('weekclaimnumber/<str:name>/',views.OneDoctorWeekLaterAllClaimsNumberView.as_view({'get':'list','post':'create'})),
]