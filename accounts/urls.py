from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.products, name="products"),
    path('account/<str:pk_test>/', views.customer, name="customer"),
    path('', views.home, name="home"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pkd>/', views.deleteOrder, name="delete_order")
]
