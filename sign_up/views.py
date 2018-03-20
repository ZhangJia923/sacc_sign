from django.shortcuts import render
from .forms import ActorInfoForm
from .models import Actor_info
from django.http import HttpResponseRedirect,Http404 #用户提交主题后我们将使用这个类将用户重新定向到网页topics
from django.urls import reverse #该函数根据指定的URL模型确定URL，这意味着Django将在页面被请求时生成url
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'sign_up/home.html')

@login_required
def actors(request):
    actors = Actor_info.objects.filter(owner=request.user).order_by('date_added')#filter(owner=request.user)指只显示本人创建的数据
    context = {'actors':actors}
    return render(request, 'sign_up/actors.html', context)



def new_actor(request):
    if request.method != 'POST':
        form = ActorInfoForm()
    else:
        form = ActorInfoForm(data=request.POST)
        if form.is_valid():
            new_actor = form.save(commit=False) #commit=False指不要提交到数据库
            new_actor.owner = request.user
            new_actor.save()
            return HttpResponseRedirect(reverse('sign_up:index'))

    context = {'form':form}
    return render(request, 'sign_up/new_actor.html', context)

@login_required
def actor(request,actor_id):
    actor = Actor_info.objects.get(id=actor_id)
    if actor.owner != request.user:
        raise Http404  #无权删除时返回404  #当访问不属于自己的信息时抛出404错误
    context = {'actor':actor}
    return render(request, 'sign_up/actor.html', context)

@login_required
def delete_actor(request,actor_id):
    actor = Actor_info.objects.get(id=actor_id)
    if actor.owner == request.user:
        Actor_info.objects.filter(id = actor_id).delete()
    else:
        raise Http404#无权删除时返回404
    return render(request,'sign_up/delete_actor.html')

@login_required
def edit_actor(request,actor_id):
    actor = Actor_info.objects.get(id=actor_id)
    if actor.owner != request.user:
        raise Http404
    if request.method == 'POST':
        college = request.POST.get('college')
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        Actor_info.objects.filter(id=actor_id).update(
            college=college,student_id=student_id,name=name,tel=tel,email=email
        )
        return HttpResponseRedirect(reverse('sign_up:actor',args=[actor_id]))

    context = {'actor':actor}
    return render(request,'sign_up/edit_actor.html',context=context)
