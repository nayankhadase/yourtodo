# Generated by Django 3.2 on 2021-05-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user_index',
            field=models.IntegerField(default=0),
        ),
    ]
