from django.urls import path

from static import views

urlpatterns = [
  path('', views.index)
]