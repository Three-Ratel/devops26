from django.shortcuts import render, redirect, HttpResponse
import hashlib
from app01 import models


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))

        obj = models.UserProfile.objects.filter(username=username, password=md5.hexdigest()).first()
        if obj:
            # 登录成功

            request.session['is_login'] = True
            request.session['user_id'] = obj.pk
            return redirect('user_list')

        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

    return render(request, 'login.html')


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        models.UserProfile.objects.create(username=username, password=md5.hexdigest())

        return redirect('user_list')

    return render(request, 'reg.html', )


def index(request):
    return HttpResponse('首页     </br> 欢迎登陆 ')


def user_list(request):
    all_user = models.UserProfile.objects.all()
    return render(request, 'user_list.html', {'all_user': all_user})


def user_edit(request):
    pk = request.GET.get('pk')
    user_obj = models.UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj.username=username
        user_obj.password=password
        user_obj.save()
        return redirect('user_list')
    return render(request, 'user_edit.html', {'user_obj': user_obj})


def user_del(request):
    pk = request.GET.get('pk')
    models.UserProfile.objects.get(pk=pk).delete()
    return redirect('user_list')
