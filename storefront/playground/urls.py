from django.urls import path
from . import views
from .views import duration_chart
#URL configuration
urlpatterns = [
    path('start/',views.index),
     path('duration-chart/', views.duration_chart, name='duration_chart')
]