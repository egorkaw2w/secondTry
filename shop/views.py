from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_protect
from admin_panel.models import Product, Order, OrderItem

@login_required
def home(request):
    return render(request, 'home/home.html')

@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'Products/products.html', {'products': products})

@login_required
def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
        total_price += subtotal
    return render(request, 'Cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    request.session['cart'] = cart
    messages.success(request, f'{product.name} добавлен в корзину!')
    return redirect('products')

@login_required
def update_cart(request, product_id):
    action = request.POST.get('action')
    cart = request.session.get('cart', {})
    if action == 'remove':
        if str(product_id) in cart:
            del cart[str(product_id)]
    elif action == 'increase':
        if str(product_id) in cart:
            cart[str(product_id)] += 1
        else:
            cart[str(product_id)] = 1
    elif action == 'decrease':
        if str(product_id) in cart and cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        elif str(product_id) in cart and cart[str(product_id)] == 1:
            del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def create_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Корзина пуста!')
        return redirect('cart')
    total_price = sum(Product.objects.get(id=pid).price * qty for pid, qty in cart.items())
    order = Order.objects.create(user=request.user, total_price=total_price, shipping_address="Адрес доставки по умолчанию")
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)
    del request.session['cart']
    messages.success(request, 'Заказ успешно создан!')
    return redirect('orders')

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'Orders/orders.html', {'orders': orders})

@csrf_protect
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Имя пользователя уже занято.')
        else:
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password)
            )
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Регистрация успешна! Вы вошли в систему.')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка аутентификации после регистрации.')
    return render(request, 'account/register.html')

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему.')
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы.')
    return redirect('home')

def admin_logout(request):
    logout(request)
    return redirect('/admin-panel/login/')