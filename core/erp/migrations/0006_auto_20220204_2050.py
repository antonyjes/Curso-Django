# Generated by Django 3.2.5 on 2022-02-05 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_category_employeecat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeecat',
            old_name='categoryId',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='employeecat',
            old_name='employeeId',
            new_name='employee',
        ),
    ]
