from django.shortcuts import render
from .forms import TeamInfoForm
from .models import Team_info,Actor_info
from users.models import User
from django.http import HttpResponseRedirect,Http404 #用户提交主题后我们将使用这个类将用户重新定向到网页topics
from django.urls import reverse #该函数根据指定的URL模型确定URL，这意味着Django将在页面被请求时生成url
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'sign_up/home.html')

# @login_required
# def actors(request):
#     lname = [str(request.user),str(request.user),str(request.user)]
#     query = "SELECT * FROM sign_up_team_info WHERE leader=%s OR member1=%s OR member2=%s"
#     teams = Team_info.objects.raw(query,params=lname)
#     context = {'teams':teams}
#     return render(request, 'sign_up/actors.html', context)

def new_team(request):
    if request.method != 'POST':
        form = TeamInfoForm()
    else:
        actor_info = Actor_info.objects.get(actor_name=request.user)
        if actor_info.is_added == True:
            context = {'actor_info':actor_info}
            return render(request,'sign_up/is_added_error.html',context)
        else:
            form = TeamInfoForm(data=request.POST)
            user = User.objects.get(username=request.user)
            if form.is_valid():
                new_actor = form.save(commit=False) #commit=False指不要提交到数据库
                new_actor.leader = user.username
                new_actor.leader_college = user.college
                new_actor.leader_tel = user.tel
                new_actor.leader_id = user.student_id
                new_actor.leader_email = user.email
                new_actor.owner = request.user
                new_actor.save()
                Actor_info.objects.filter(actor_name=request.user).update(
                    is_added=True, team_name=new_actor.team_name
                )
                return HttpResponseRedirect(reverse('sign_up:index'))

    context = {'form':form}
    return render(request, 'sign_up/new_team.html', context)


def my_team(request):
    lname = [str(request.user), str(request.user), str(request.user)]
    query = "SELECT * FROM sign_up_team_info WHERE leader=%s OR member1=%s OR member2=%s"
    teams = Team_info.objects.raw(query, params=lname)
    context = {'teams': teams}
    return render(request, 'sign_up/team.html', context)



# @login_required
# def actor(request,actor_id):
#     team = Team_info.objects.get(id=actor_id)
#     if str(team.owner) != str(request.user) and str(team.member1) != str(request.user) and str(team.member2) != str(request.user):
#         raise Http404  #无权删除时返回404  #当访问不属于自己的信息时抛出404错误
#     context = {'team':team}
#     return render(request, 'sign_up/team.html', context)

@login_required
def delete_actor(request,actor_id):
    actor = Team_info.objects.get(id=actor_id)
    if actor.owner == request.user:
        Actor_info.objects.filter(actor_name=actor.member1).update(
            is_added=False, team_name=''
        )
        Actor_info.objects.filter(actor_name=actor.member2).update(
            is_added=False, team_name=''
        )
        Actor_info.objects.filter(actor_name=actor.leader).update(
            is_added=False, team_name=''
        )
        Team_info.objects.filter(id = actor_id).delete()
    else:
        return render(request,'sign_up/delete_error.html')
    return render(request,'sign_up/delete_actor.html')

@login_required
def edit_team(request,team_id):
    team = Team_info.objects.get(id=team_id)
    if str(team.owner) != str(request.user):
        return render(request,'sign_up/edit_error.html')
    if request.method == 'POST':
        college = request.POST.get('college')
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        Team_info.objects.filter(id=team_id).update(
            college=college,student_id=student_id,name=name,tel=tel,email=email
        )
        return HttpResponseRedirect(reverse('sign_up:my_team',args=[team_id]))

    context = {'team':team}
    return render(request,'sign_up/edit_actor.html',context)

@login_required
def add_team(request,team_id):

    team = Team_info.objects.get(id=team_id)

    actor_info = Actor_info.objects.get(actor_name=request.user)

    user = User.objects.get(username=request.user)

    if actor_info.is_added == True:
        context = {'actor_info':actor_info}
        return render(request,'sign_up/is_added_error.html',context)#############

    member = user.username
    college = user.college
    tel = user.tel
    student_id = user.student_id
    email = user.email


    if team.member1 is '':
        Team_info.objects.filter(id=team_id).update(
            member1=member, college1=college, tel1=tel, student_id1=student_id, email1=email
        )
        Actor_info.objects.filter(actor_name=request.user).update(
            is_added=True,team_name=team.team_name
        )
    else:
        Team_info.objects.filter(id=team_id).update(
            member2=member, college2=college, tel2=tel, student_id2=student_id, email2=email
        )
        Actor_info.objects.filter(actor_name=request.user).update(
            is_added=True, team_name=team.team_name
        )

    return HttpResponseRedirect(reverse('sign_up:index'))

@login_required
def quit_team(request,team_id):
    team = Team_info.objects.get(id=team_id)

    actor_info = Actor_info.objects.get(actor_name=request.user)

    user = User.objects.get(username=request.user)

    if actor_info.is_added == False:
        is_added = actor_info.is_added
        context = {'is_added':is_added}
        return render(request, 'sign_up/is_added_error.html',context)

    if team.member1 == actor_info.actor_name:
        Team_info.objects.filter(id=team_id).update(
            member1='', college1='', tel1='', student_id1='', email1=''
        )
        Actor_info.objects.filter(actor_name=request.user).update(
            is_added=False, team_name=''
        )
    else:
        Team_info.objects.filter(id=team_id).update(
            member2='', college2='', tel2='', student_id2='', email2=''
        )
        Actor_info.objects.filter(actor_name=request.user).update(
            is_added=False, team_name=''
        )

    return HttpResponseRedirect(reverse('sign_up:index'))


@login_required
def teams(request):
    teams = Team_info.objects.all()
    if teams:
        try:
            actor_info = Actor_info.objects.get(actor_name=request.user)
        except:
            actor_info = None
        context = {'teams':teams,'actor_info':actor_info}
        return render(request,'sign_up/teams.html',context)
    else:
        actor_info = None
        context = {'teams': teams, 'actor_info': actor_info}
        return render(request, 'sign_up/teams.html', context)