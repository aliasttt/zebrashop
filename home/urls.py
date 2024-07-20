
from django.urls import path
from . import views

urlpatterns = [
    path("demo",views.demo),
    path('home',views.homehtml),
    
    path('login',views.AccountFormViews,)
]