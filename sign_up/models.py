from django.db import models
# from django.contrib.auth.models import User
from users.models import User
# Create your models here.
class Team_info(models.Model):

    team_name = models.CharField(max_length=50)

    leader = models.CharField(max_length=50, default=None, blank=True)
    leader_college = models.CharField(max_length=50, default=None, blank=True)
    leader_tel = models.CharField(max_length=11, default=None, blank=True)
    leader_id = models.CharField(max_length=9, default=None, blank=True)
    leader_email = models.EmailField(default=None, blank=True)

    member1 = models.CharField(max_length=50,default=None,blank=True)
    college1 = models.CharField(max_length=50,default=None,blank=True)
    tel1 = models.CharField(max_length=11,default=None,blank=True)
    student_id1 = models.CharField(max_length=9,default=None,blank=True)
    email1 = models.EmailField(default=None,blank=True)

    member2 = models.CharField(max_length=50,default=None,blank=True)
    college2 = models.CharField(max_length=50,default=None,blank=True)
    tel2 = models.CharField(max_length=11,default=None,blank=True)
    student_id2 = models.CharField(max_length=9,default=None,blank=True)
    email2 = models.EmailField(default=None,blank=True)

    team_key = models.CharField(default=None,max_length=10)

    is_added = models.BooleanField(default=False)


    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name

