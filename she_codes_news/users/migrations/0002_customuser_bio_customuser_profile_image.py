# Generated by Django 4.2.2 on 2023-12-03 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.URLField(blank=True),
        ),
    ]
