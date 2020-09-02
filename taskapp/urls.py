from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('other_page', views.other_page, name='other_page')
]