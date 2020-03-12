# Generated by Django 3.0.2 on 2020-02-27 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mathematorApp', '0003_delete_exercisedone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idExercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromExercise', to='mathematorApp.Exercise')),
                ('idExerciseRequirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toExercise', to='mathematorApp.Exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='relation',
            field=models.ManyToManyField(related_name='related_to', through='mathematorApp.ExerciseRequirement', to='mathematorApp.Exercise'),
        ),
    ]