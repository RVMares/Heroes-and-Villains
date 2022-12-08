from django.urls import path
from . import views

urlpatterns = [
    # path('', views.pass)
    path('<int:pk>/', views.supers_detail)
]