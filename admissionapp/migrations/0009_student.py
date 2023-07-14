# Generated by Django 4.2.1 on 2023-05-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissionapp', '0008_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('mother_name', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone_number', models.CharField(max_length=20)),
                ('alt_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('sslc_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sslc_school', models.CharField(max_length=100, null=True)),
                ('puc_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('puc_college', models.CharField(max_length=100, null=True)),
                ('selected_college', models.CharField(default='empty', max_length=100)),
                ('selected_course', models.CharField(default='empty', max_length=100)),
                ('photo', models.ImageField(default='default.jpg', upload_to='media/')),
            ],
        ),
    ]