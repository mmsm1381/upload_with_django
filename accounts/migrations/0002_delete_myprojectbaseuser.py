# Generated by Django 4.0.1 on 2022-01-04 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_upload', '0002_alter_flile_user'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyProjectBaseUser',
        ),
    ]
