from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from admin_panel.models import Category, Material, Product, Order, OrderItem, Role, UserRole, Review, Payment
from .serializers import (
    CategorySerializer, MaterialSerializer, ProductSerializer, OrderSerializer,
    OrderItemSerializer, RoleSerializer, UserRoleSerializer, ReviewSerializer, PaymentSerializer
)
from .permissions import (
    CustomCategoryPermissions, CustomMaterialPermissions, CustomProductPermissions,
    CustomOrderPermissions, CustomOrderItemPermissions, CustomRolePermissions,
    CustomUserRolePermissions, CustomReviewPermissions, CustomPaymentPermissions
)
import logging

# Настройка логгера
logger = logging.getLogger(__name__)

# Пагинация
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomCategoryPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"CategoryViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class MaterialViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [CustomMaterialPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"MaterialViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class ProductViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomProductPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"ProductViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class OrderViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomOrderPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"OrderViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(user__username__icontains=search_query)
        return queryset

class OrderItemViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [CustomOrderItemPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"OrderItemViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(product__name__icontains=search_query)
        return queryset

class RoleViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [CustomRolePermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"RoleViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class UserRoleViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [CustomUserRolePermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"UserRoleViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(user__username__icontains=search_query)
        return queryset

class ReviewViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CustomReviewPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"ReviewViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(comment__icontains=search_query)
        return queryset

class PaymentViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [CustomPaymentPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"PaymentViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(transaction_id__icontains=search_query)
        return queryset