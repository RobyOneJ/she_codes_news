# Generated by Django 4.2.2 on 2023-12-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_newsstory_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]