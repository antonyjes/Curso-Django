# Generated by Django 3.2.5 on 2022-02-05 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_remove_employee_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'tipo',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp.type'),
        ),
    ]
