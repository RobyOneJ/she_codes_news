# Generated by Django 4.2.2 on 2023-12-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_newsstory_category_alter_newsstory_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
