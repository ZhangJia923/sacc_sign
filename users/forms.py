from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','college','student_id','tel']
        labels = {
            'username':'请输入姓名',
            'email':'请输入邮箱',
            'college':'请输入学院',
            'student_id':'请输入学号',
            'tel':'请输入手机号',
        }