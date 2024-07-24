
from django.contrib import admin
from django.urls import path , include

app_name = 'home'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls', namespace='home')), 
]