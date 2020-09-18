from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.products, name="products"),
    path('account/<str:pk_test>/', views.customer, name="customer"),
    path('', views.home, name="home"),
]
