# Generated by Django 2.2 on 2020-11-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_staff_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='direction',
            field=models.ManyToManyField(blank=True, to='projects.Direction'),
        ),
    ]
