# Generated by Django 4.2 on 2023-06-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0030_application_date_user_phone_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
    ]
