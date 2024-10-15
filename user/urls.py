from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('add_user/', views.add_user, name='add_user')

]