# Generated by Django 4.2.1 on 2023-05-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0003_students_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='selected_college',
            field=models.CharField(default='empty', max_length=100),
        ),
        migrations.AddField(
            model_name='students',
            name='selected_course',
            field=models.CharField(default='empty', max_length=100),
        ),
    ]
