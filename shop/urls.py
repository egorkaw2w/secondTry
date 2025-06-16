from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('products/', views.products, name='products'),
    # path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]