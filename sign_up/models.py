from django.db import models
# from django.contrib.auth.models import User
from users.models import User
# Create your models here.
class Actor_info(models.Model):

    team_name = models.CharField(max_length=50)

    # leader = models.ForeignKey(User.username, on_delete=models.CASCADE)
    # leader_college = models.ForeignKey(User.college, on_delete=models.CASCADE)
    # leader_tel = models.ForeignKey(User.tel, on_delete=models.CASCADE)
    # leader_id = models.ForeignKey(User.student_id, on_delete=models.CASCADE)
    # leader_email = models.ForeignKey(User.email, on_delete=models.CASCADE)

    member1 = models.CharField(max_length=50,default=None)
    college1 = models.CharField(max_length=50,default=None)
    tel1 = models.CharField(max_length=11,default=None)
    student_id1 = models.CharField(max_length=9,default=None)
    email1 = models.EmailField(default=None)

    member2 = models.CharField(max_length=50,default=None)
    college2 = models.CharField(max_length=50,default=None)
    tel2 = models.CharField(max_length=11,default=None)
    student_id2 = models.CharField(max_length=9,default=None)
    email2 = models.EmailField(default=None)


    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name