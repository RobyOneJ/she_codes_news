# Generated by Django 4.2.2 on 2023-12-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_remove_newsstory_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]