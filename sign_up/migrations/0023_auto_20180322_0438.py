# Generated by Django 2.0.3 on 2018-03-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0022_auto_20180322_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_info',
            name='leader',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='team_info',
            name='leader_college',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='team_info',
            name='leader_email',
            field=models.EmailField(blank=True, default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='team_info',
            name='leader_id',
            field=models.CharField(blank=True, default=None, max_length=9),
        ),
        migrations.AddField(
            model_name='team_info',
            name='leader_tel',
            field=models.CharField(blank=True, default=None, max_length=11),
        ),
    ]
