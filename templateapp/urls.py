from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home,name='home'),
    path('house/',House,name='house'),
    path('death/',death,name='death'),
]
