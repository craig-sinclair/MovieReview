# Generated by Django 5.0.6 on 2024-05-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_alter_customuser_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(unique=True)),
            ],
        ),
    ]
