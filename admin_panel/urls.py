from django.contrib import admin
from django.urls import path, include
from admin_panel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.admin_home, name='admin_home'),
    path('admin-panel/<str:model_name>/', views.admin_list, name='admin_list'),
    path('admin-panel/<str:model_name>/create/', views.admin_create, name='admin_create'),
    path('admin-panel/<str:model_name>/<int:object_id>/update/', views.admin_update, name='admin_update'),
    path('admin-panel/<str:model_name>/<int:object_id>/delete/', views.admin_delete, name='admin_delete'),
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/logout/', views.admin_logout, name='admin_logout'),
    path('shop/', include('shop.urls')),
]