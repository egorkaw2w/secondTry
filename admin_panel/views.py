from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import ModelForm
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import logging
from .forms import CategoryForm, MaterialForm, ProductForm, OrderForm, OrderItemForm, RoleForm, UserRoleForm, ReviewForm, PaymentForm

logger = logging.getLogger(__name__)

# Словарь соответствия русских названий моделям
model_name_mapping = {
    'Категории': 'category',
    'Материалы': 'material',
    'Товары': 'product',  # Добавлено
    'Заказы': 'order',
    'ЭлементыЗаказа': 'orderitem',
    'Роли': 'role',
    'РолиПользователя': 'userrole',  # Добавлено
    'Отзывы': 'review',
    'Платежи': 'payment',
}

@login_required
def admin_home(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/shop/')
    try:
        models = apps.get_app_config('admin_panel').get_models()
        model_list = [{'name': model._meta.model_name, 'verbose_name': model._meta.verbose_name_plural} for model in models]
        logger.info(f"Loaded models: {model_list}")
        if not model_list:
            logger.warning("No models found in 'admin_panel' app config.")
    except Exception as e:
        logger.error(f"Error loading models: {str(e)}")
        model_list = []
    return render(request, 'home/admin_home.html', {'model_list': model_list})

@login_required
def admin_list(request, model_name):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    try:
        models = apps.get_app_config('admin_panel').get_models()
        model_list = [{'name': model._meta.model_name, 'verbose_name': model._meta.verbose_name_plural} for model in models]
    except Exception as e:
        logger.error(f"Error loading models: {str(e)}")
        model_list = []
    english_model_name = model_name_mapping.get(model_name, model_name.lower())
    model = apps.get_model('admin_panel', english_model_name)
    objects = model.objects.all()
    fields = [f for f in model._meta.fields if f.name not in ['id', 'created_at', 'updated_at']]
    return render(request, 'Admin-panel/adminka.html', {
        'operation': 'List',
        'model_name': model._meta.verbose_name_plural,
        'objects': objects,
        'fields': fields,
        'model_list': model_list
    })

@login_required
def admin_create(request, model_name):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    try:
        models = apps.get_app_config('admin_panel').get_models()
        model_list = [{'name': model._meta.model_name, 'verbose_name': model._meta.verbose_name_plural} for model in models]
    except Exception as e:
        logger.error(f"Error loading models: {str(e)}")
        model_list = []
    english_model_name = model_name_mapping.get(model_name, model_name.lower())
    model_forms = {
        'category': CategoryForm,
        'material': MaterialForm,
        'product': ProductForm,
        'order': OrderForm,
        'orderitem': OrderItemForm,
        'role': RoleForm,
        'userrole': UserRoleForm,
        'review': ReviewForm,
        'payment': PaymentForm,
    }
    FormClass = model_forms.get(english_model_name)
    if not FormClass:
        raise ValueError(f"No form defined for model '{english_model_name}'")
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{FormClass._meta.model._meta.verbose_name} создан!')
            return redirect('admin_list', model_name=english_model_name)
    else:
        form = FormClass()
    return render(request, 'Admin-panel/adminka.html', {
        'operation': 'Создать',
        'model_name': model_name,
        'form': form,
        'model_list': model_list
    })

@login_required
def admin_update(request, model_name, object_id):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    try:
        models = apps.get_app_config('admin_panel').get_models()
        model_list = [{'name': model._meta.model_name, 'verbose_name': model._meta.verbose_name_plural} for model in models]
    except Exception as e:
        logger.error(f"Error loading models: {str(e)}")
        model_list = []
    english_model_name = model_name_mapping.get(model_name, model_name.lower())
    model_forms = {
        'category': CategoryForm,
        'material': MaterialForm,
        'product': ProductForm,
        'order': OrderForm,
        'orderitem': OrderItemForm,
        'role': RoleForm,
        'userrole': UserRoleForm,
        'review': ReviewForm,
        'payment': PaymentForm,
    }
    FormClass = model_forms.get(english_model_name)
    if not FormClass:
        raise ValueError(f"No form defined for model '{english_model_name}'")
    model = apps.get_model('admin_panel', english_model_name)
    obj = get_object_or_404(model, id=object_id)
    if request.method == 'POST':
        form = FormClass(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'{model._meta.verbose_name} обновлён!')
            return redirect('admin_list', model_name=english_model_name)
    else:
        form = FormClass(instance=obj)
    return render(request, 'Admin-panel/adminka.html', {
        'operation': 'Редактировать',
        'model_name': model_name,
        'form': form,
        'model_list': model_list
    })

@login_required
def admin_delete(request, model_name, object_id):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    try:
        models = apps.get_app_config('admin_panel').get_models()
        model_list = [{'name': model._meta.model_name, 'verbose_name': model._meta.verbose_name_plural} for model in models]
    except Exception as e:
        logger.error(f"Error loading models: {str(e)}")
        model_list = []
    english_model_name = model_name_mapping.get(model_name, model_name.lower())
    model = apps.get_model('admin_panel', english_model_name)
    obj = get_object_or_404(model, id=object_id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f'{model._meta.verbose_name} удалён!')
        return redirect('admin_list', model_name=english_model_name)
    return render(request, 'Admin-panel/adminka.html', {
        'operation': 'Удалить',
        'model_name': model_name,
        'form': {'name': obj._meta.model_name, 'id': obj.id},
        'model_list': model_list
    })

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/admin-panel/' if user.is_superuser else '/shop/')
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'account/admin_login.html', {'next': request.GET.get('next', '')})

def admin_logout(request):
    logout(request)
    return redirect('/admin-panel/login/')