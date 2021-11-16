from django.urls import path
from app222.views import *
app_name='app222'
urlpatterns=[
    path('raina/',raina,name='raina'),
]