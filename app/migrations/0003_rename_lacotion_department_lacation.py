# Generated by Django 4.1.2 on 2022-10-15 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_fole_employee_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='lacotion',
            new_name='lacation',
        ),
    ]
