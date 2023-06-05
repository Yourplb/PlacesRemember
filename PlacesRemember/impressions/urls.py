from django.urls import path, include
from . import views


app_name = 'impressions'


urlpatterns = [
    path('', views.index, name='index'),
    path('impressions/', views.impressions_list, name='impressions'),
]
