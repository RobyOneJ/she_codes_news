# Generated by Django 4.2.2 on 2023-12-04 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_newsstory_update_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsstory',
            old_name='Update_date',
            new_name='last_update',
        ),
    ]
