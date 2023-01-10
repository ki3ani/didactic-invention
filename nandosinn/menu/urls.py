from django.urls import path
from . import views

urlpatterns = [
    path('/menu', views.MenuItemsList.as_view()),
    path('<int:pk>/', views.SingleMenuItem.as_view()),
]




