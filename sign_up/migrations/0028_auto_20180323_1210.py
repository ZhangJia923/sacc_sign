# Generated by Django 2.0.3 on 2018-03-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0027_auto_20180322_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_info',
            name='team_key',
            field=models.CharField(default=None, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='team_info',
            name='team_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]