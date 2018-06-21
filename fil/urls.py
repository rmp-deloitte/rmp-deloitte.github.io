from django.urls import path
from . import views

app_name='fil'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
]
