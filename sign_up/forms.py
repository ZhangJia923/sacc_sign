from django import forms
from .models import Team_info

class TeamInfoForm(forms.ModelForm):
    class Meta:#储存管理模型的额外信息
        model = Team_info

        # 用来表示在前端使用form时显示哪些，就像本行表示，name，student_id，college显示而日期不显示
        fields = [
            'team_name','member1','college1','tel1','student_id1','email1','member2','college2','tel2','student_id2','email2',
        ]

        # 用来表示表单前的介绍如不加则默认为数据库中字段的名字如name，student_id等等，使用label则前面则显示你设着的
        labels = {
            'team_name':'请输入队伍名称',
            'college1':'请输入队员一的学院',
            'student_id1':'请输入队员一的学号',
            'member1':'请输入队员一的姓名',
            'tel1':'请输入队员一的手机号',
            'email1':'请输入队员一的邮箱',
            'college2': '请输入队员二的学院',
            'student_id2': '请输入队员二的学号',
            'member2': '请输入队员二的姓名',
            'tel2': '请输入队员二的手机号',
            'email2': '请输入队员二的邮箱'
        }


