# Generated by Django 5.2.3 on 2025-07-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_course_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
