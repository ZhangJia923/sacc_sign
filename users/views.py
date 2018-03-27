from django.shortcuts import render
from .forms import UserForm
from sign_up.models import Actor_info
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('sign_up:index'))
        else:
            return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request,'users/login.html')

# @csrf_protect
def register(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            new_user = form.save()
            # 如果认证信息有效，会返回一个  User  对象。authenticate()会在User 对象上设置一个属性标识那种认证后端认证了该用户，
            # 且该信息在后面的登录过程中是需要的。当我们试图登陆一个从数据库中直接取出来不经过authenticate()的User对象会报错的！！
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            actor_info = Actor_info()
            actor_info.actor_id = new_user.username
            actor_info.team_name = '无'
            actor_info.is_added = False
            actor_info.save()
            user = request.user
            # user.is_active = False
            user.save()
            email = [user.email]
            print(email)
            send_mail('测试一下', '这次能不能成功？？', 'zhjia97@163.com', email, fail_silently=False)
            return HttpResponseRedirect(reverse('sign_up:index'))

    context = {'form':form}
    return render(request,'users/register.html',context)

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('sign_up:index'))