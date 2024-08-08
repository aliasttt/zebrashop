
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


app_name = 'home'

urlpatterns = [
    path("demo",views.demo),
    path('tarefe_barbary',views.tarefe_barbary, name = "tarefe_barbary"),
    path('', views.homehtml, name='homehtml'),
    path('login',views.AccountFormViews,name="account"),
    path('darbare_ma',views.contact_us,name='contact_us'),
    path('soalat_motadavel',views.soalat_motadavel,name="soalat_motadavel"),
    path('ghavanin_moghararat',views.ghavanin,name="ghavanin"),
    path('shiveh_pardakht',views.siveh_pardakht,name='shiveh_pardakht'),
    
    path('products/', views.product_list, name='mardane'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)