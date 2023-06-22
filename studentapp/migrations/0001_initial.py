# Generated by Django 4.2.1 on 2023-06-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=10, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('class_level', models.CharField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd')], max_length=2)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='student_images/')),
                ('marklist', models.FileField(upload_to='marklists/')),
            ],
        ),
    ]
