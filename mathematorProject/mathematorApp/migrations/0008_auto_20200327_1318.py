# Generated by Django 3.0.2 on 2020-03-27 13:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathematorApp', '0007_auto_20200327_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseoperation',
            name='operators',
            field=models.CharField(default='+', max_length=4, validators=[django.core.validators.RegexValidator('^[\\+\\*\\/\\-]*$')]),
        ),
    ]
