# Generated by Django 5.2.4 on 2025-07-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp', models.CharField(max_length=100)),
                ('telegram', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
            ],
        ),
    ]
