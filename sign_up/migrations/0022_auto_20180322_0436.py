# Generated by Django 2.0.3 on 2018-03-22 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0021_auto_20180322_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_info',
            name='leader',
        ),
        migrations.RemoveField(
            model_name='team_info',
            name='leader_college',
        ),
        migrations.RemoveField(
            model_name='team_info',
            name='leader_email',
        ),
        migrations.RemoveField(
            model_name='team_info',
            name='leader_id',
        ),
        migrations.RemoveField(
            model_name='team_info',
            name='leader_tel',
        ),
    ]
