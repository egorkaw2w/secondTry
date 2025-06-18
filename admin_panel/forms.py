from django import forms
from .models import Category, Material, Product, Order, OrderItem, Role, UserRole, Review, Payment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название категории', 'style': 'width: 300px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите описание', 'style': 'width: 300px;'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название материала', 'style': 'width: 300px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите описание', 'style': 'width: 300px;'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара', 'style': 'width: 300px;'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'materials': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'width: 300px; height: 100px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите описание', 'style': 'width: 300px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'style': 'width: 300px;'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-control-checkbox'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'style': 'width: 300px;'}),
            'status': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'shipping_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите адрес доставки', 'style': 'width: 300px;'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
        widgets = {
            'order': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'product': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'style': 'width: 300px;'}),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название роли', 'style': 'width: 300px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите описание роли', 'style': 'width: 300px;'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'role': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'assigned_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'user': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5, 'style': 'width: 300px;'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите комментарий', 'style': 'width: 300px;'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'order': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'style': 'width: 300px;'}),
            'method': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'status': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'transaction_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ID транзакции', 'style': 'width: 300px;'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }