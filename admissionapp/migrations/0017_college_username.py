# Generated by Django 4.2.1 on 2023-06-17 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0016_rename_reviews_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
