# Generated by Django 2.0 on 2020-04-14 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='songimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]