# Generated by Django 4.2.1 on 2023-05-21 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0007_rename_studentss_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
