from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('bunkering/', BunkeringView.as_view(), name="bunkering"),
    path('concern/', ConcernView.as_view(), name="concern"),
    path('team/', TeamView.as_view(), name='team'),
    path('career/', CareerView.as_view(), name='career'),
    path('quote/', RequestQuotationView.as_view(), name='quote'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('terms/', TermsAndConditionView.as_view(), name='terms')
]
