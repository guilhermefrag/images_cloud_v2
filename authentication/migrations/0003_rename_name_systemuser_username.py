# Generated by Django 4.1.3 on 2022-11-24 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_user_systemuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemuser',
            old_name='name',
            new_name='username',
        ),
    ]