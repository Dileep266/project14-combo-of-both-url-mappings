from specific.views import *
from django.urls import path
app_name='specific'

urlpatterns=[
    path('darling/',darling,name='darling'),
    path('bahubali/',bahubali,name='bahubali'),
]