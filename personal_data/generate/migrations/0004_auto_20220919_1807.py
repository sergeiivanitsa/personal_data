# Generated by Django 2.2.19 on 2022-09-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate', '0003_auto_20220916_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='birth_date',
            field=models.DateField(default='Day/Month/Year'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='contract_date',
            field=models.DateField(default='Day/Month/Year'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='issue_date',
            field=models.DateField(default='Day/Month/Year'),
        ),
    ]