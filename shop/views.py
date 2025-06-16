from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    return render(request, 'home/home.html')

# def products(request):
#     return render(request, 'products.html')
#
# def cart(request):
#     return render(request, 'cart.html')

@csrf_protect
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')  # Опционально, может быть пустым

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Имя пользователя уже занято.')
        else:
            # Создаём пользователя с хешированным паролем
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password)
            )
            # Аутентифицируем и логиним пользователя
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