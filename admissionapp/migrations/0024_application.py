# Generated by Django 4.2 on 2023-06-24 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0023_remove_student_status_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('applied_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applied_by', to=settings.AUTH_USER_MODEL)),
                ('applied_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applied_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]