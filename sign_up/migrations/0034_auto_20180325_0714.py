# Generated by Django 2.0.3 on 2018-03-25 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0033_auto_20180325_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_info',
            name='tel1',
            field=models.CharField(blank=True, default=None, max_length=11, null=True),
        ),
    ]
