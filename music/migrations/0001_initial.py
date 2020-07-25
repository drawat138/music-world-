# Generated by Django 2.2 on 2020-05-20 11:45

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Godsong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('singer', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(upload_to=music.models.upload_picture)),
                ('link', models.URLField(blank=True)),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('time', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrumental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('songname', models.CharField(blank=True, max_length=100, null=True)),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True)),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('time', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=35, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('confirm_password', models.CharField(max_length=10)),
            ],
        ),
    ]