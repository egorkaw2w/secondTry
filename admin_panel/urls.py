from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('login/', views.admin_login, name='admin_login'),
    path('<str:model_name>/', views.admin_list, name='admin_list'),
    path('<str:model_name>/create/', views.admin_create, name='admin_create'),
    path('<str:model_name>/update/<int:object_id>/', views.admin_update, name='admin_update'),
    path('<str:model_name>/delete/<int:object_id>/', views.admin_delete, name='admin_delete'),
]