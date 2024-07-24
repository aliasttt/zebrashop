
from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path("demo",views.demo),
    path('tarefe_barbary',views.tarefe_barbary, name = "tarefe_barbary"),
    path('', views.homehtml, name='homehtml'),
    path('login',views.AccountFormViews,name="account")
]