from django.urls import path
from . import views


app_name = 'impressions'


urlpatterns = [
    path('', views.index, name='index'),
    path('impressions/', views.impressions_list, name='impressions'),
    path('impressions_create/', views.impressions_create, name='impressions_create'),
]
