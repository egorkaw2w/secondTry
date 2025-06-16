from django.contrib import admin
from .models import Category, Material, Product, Cart, Order, OrderItem, Payment, Review

# Регистрация моделей
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Review)