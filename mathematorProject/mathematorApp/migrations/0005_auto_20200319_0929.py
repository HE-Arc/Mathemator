# Generated by Django 3.0.2 on 2020-03-19 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathematorApp', '0004_auto_20200319_0757'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExerciseFixDonneeResultat',
            new_name='ExerciseFix',
        ),
        migrations.RenameModel(
            old_name='ExerciseSimpleOperation',
            new_name='ExerciseOperations',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='donnee',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='exerciseoperations',
            old_name='nbOperation',
            new_name='nbOperators',
        ),
    ]
