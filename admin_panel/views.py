from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import ModelForm
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

@login_required
def admin_home(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    models = apps.get_app_config('shop').get_models()
    model_list = [{'name': model._meta.model_name, 'verbose_name': model._meta.verbose_name_plural} for model in models]
    return render(request, 'home/admin_home.html', {'model_list': model_list})

@login_required
def admin_list(request, model_name):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    model = apps.get_model('shop', model_name)
    objects = model.objects.all()
    fields = [f for f in model._meta.fields if f.name not in ['id', 'created_at', 'updated_at']]
    return render(request, 'home/admin_home.html', {
        'operation': 'List',
        'model_name': model._meta.verbose_name_plural,
        'objects': objects,
        'fields': fields
    })

@login_required
def admin_create(request, model_name):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    model = apps.get_model('shop', model_name)
    if request.method == 'POST':
        form = ModelForm(request.POST, model=model)
        if form.is_valid():
            form.save()
            messages.success(request, f'{model._meta.verbose_name} создан!')
            return redirect('admin_list', model_name=model_name)
    else:
        form = ModelForm(model=model)
    return render(request, 'Admin-panel/adminka.html', {
        'operation': 'Создать',
        'model_name': model._meta.verbose_name,
        'form': form
    })

@login_required
def admin_update(request, model_name, object_id):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    model = apps.get_model('shop', model_name)
    obj = get_object_or_404(model, id=object_id)
    if request.method == 'POST':
        form = ModelForm(request.POST, instance=obj, model=model)
        if form.is_valid():
            form.save()
            messages.success(request, f'{model._meta.verbose_name} обновлён!')
            return redirect('admin_list', model_name=model_name)
    else:
        form = ModelForm(instance=obj, model=model)
    return render(request, 'Admin-panel/adminka.html', {
        'operation': 'Редактировать',
        'model_name': model._meta.verbose_name,
        'form': form
    })

@login_required
def admin_delete(request, model_name, object_id):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin-panel/login/?next=' + request.path)
    model = apps.get_model('shop', model_name)
    obj = get_object_or_404(model, id=object_id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f'{model._meta.verbose_name} удалён!')
        return redirect('admin_list', model_name=model_name)
    return render(request, 'Admin-panel/adminka.html', {
        'operation': 'Удалить',
        'model_name': model._meta.verbose_name,
        'form': {'name': obj._meta.model_name, 'id': obj.id}
    })

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                next_url = request.GET.get('next', '/admin-panel/')
                return HttpResponseRedirect(next_url)
            else:
                messages.error(request, 'Только суперпользователи имеют доступ.')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'account/login.html', {'next': request.GET.get('next', '')})