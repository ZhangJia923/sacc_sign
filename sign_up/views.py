from django.shortcuts import render
from .forms import TeamInfoForm
from .models import Team_info
from users.models import User
from django.http import HttpResponseRedirect,Http404 #用户提交主题后我们将使用这个类将用户重新定向到网页topics
from django.urls import reverse #该函数根据指定的URL模型确定URL，这意味着Django将在页面被请求时生成url
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'sign_up/home.html')

@login_required
def actors(request):
    actors = Team_info.objects.filter(owner=request.user).order_by('date_added')#filter(owner=request.user)指只显示本人创建的数据
    context = {'actors':actors}
    return render(request, 'sign_up/actors.html', context)



def new_actor(request):
    if request.method != 'POST':
        form = TeamInfoForm()
    else:
        form = TeamInfoForm(data=request.POST)
        user = User.objects.filter()
        if form.is_valid():
            new_actor = form.save(commit=False) #commit=False指不要提交到数据库
            new_actor.leader = user[1].username
            new_actor.leader_college = user[1].college
            new_actor.leader_tel = user[1].tel
            new_actor.leader_id = user[1].student_id
            new_actor.leader_email = user[1].email
            new_actor.owner = request.user
            new_actor.save()
            return HttpResponseRedirect(reverse('sign_up:index'))

    context = {'form':form}
    return render(request, 'sign_up/new_actor.html', context)

@login_required
def actor(request,actor_id):
    actor = Team_info.objects.get(id=actor_id)
    if actor.owner != request.user:
        raise Http404  #无权删除时返回404  #当访问不属于自己的信息时抛出404错误
    context = {'actor':actor}
    return render(request, 'sign_up/actor.html', context)

@login_required
def delete_actor(request,actor_id):
    actor = Team_info.objects.get(id=actor_id)
    if actor.owner == request.user:
        Team_info.objects.filter(id = actor_id).delete()
    else:
        raise Http404#无权删除时返回404
    return render(request,'sign_up/delete_actor.html')

@login_required
def edit_actor(request,actor_id):
    actor = Team_info.objects.get(id=actor_id)
    if actor.owner != request.user:
        raise Http404
    if request.method == 'POST':
        college = request.POST.get('college')
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        Team_info.objects.filter(id=actor_id).update(
            college=college,student_id=student_id,name=name,tel=tel,email=email
        )
        return HttpResponseRedirect(reverse('sign_up:actor',args=[actor_id]))

    context = {'actor':actor}
    return render(request,'sign_up/edit_actor.html',context=context)

@login_required
def add_team(request,team_id):

    team = Team_info.objects.get(id=team_id)

    actor_info = Team_info(team_name=team.team_name,is_added=False)
    # Team_info.objects.create(team_name=actor_info.team_name,is_added=actor_info.is_added)
    actor_info = Team_info.objects.get(owner=request.user)

    user = User.objects.filter()

    if actor_info.is_added == True:
        return render(request,'sign_up/is_added_error.html')

    member = user[1].username
    college = user[1].college
    tel = user[1].tel
    student_id = user[1].student_id
    email = user[1].email


    if team.member1 is '':
        Team_info.objects.filter(id=team_id).update(
            member1=member, college1=college, tel1=tel, student_id1=student_id, email1=email,is_added=True
        )
        Team_info.objects.filter(owner=request.user).update(
            is_added=True,team_name=team.team_name
        )
    else:
        Team_info.objects.filter(id=team_id).update(
            member2=member, college2=college, tel2=tel, student_id2=student_id, email2=email,is_added=True
        )

    return HttpResponseRedirect(reverse('sign_up:index'))

@login_required
def quit_team(request,team_id):
    team = Team_info.objects.get(id=team_id)

    actor_info = Team_info.objects.get(owner=request.user)

    user = User.objects.filter()

    if actor_info.is_added == False:
        is_added = actor_info.is_added
        context = {'is_added':is_added}
        return render(request, 'sign_up/is_added_error.html',context)

    member = user[1].username
    college = user[1].college
    tel = user[1].tel
    student_id = user[1].student_id
    email = user[1].email

    if team.member1 is actor_info.owner.username:
        Team_info.objects.filter(id=team_id).update(
            member1='', college1='', tel1='', student_id1='', email1=''
        )
        Team_info.objects.filter(owner=request.user).update(
            is_added=True, team_name=team.team_name
        )
    else:
        Team_info.objects.filter(id=team_id).update(
            member2='', college2='', tel2='', student_id2='', email2=''
        )

    return HttpResponseRedirect(reverse('sign_up:index'))


@login_required
def teams(request):
    teams = Team_info.objects.all()
    if teams:
        actor_info = Team_info.objects.get(owner=request.user)
        context = {'teams':teams,'actor_info':actor_info}
        return render(request,'sign_up/teams.html',context)
    else:
        actor_info = None
        context = {'teams': teams, 'actor_info': actor_info}
        return render(request, 'sign_up/teams.html', context)