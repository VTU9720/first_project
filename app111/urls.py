from django.urls import path
from app111.views import *
app_name='app111'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]