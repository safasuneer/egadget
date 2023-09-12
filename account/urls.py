from django.urls import path,include
from .views import *

urlpatterns=[
    path('userreg',UserRegView.as_view(),name="reg"),
    path('lgout',LgOutView.as_view(),name="lgout")
    
    

]