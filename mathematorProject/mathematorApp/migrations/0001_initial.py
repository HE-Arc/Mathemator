# Generated by Django 3.0.2 on 2020-03-15 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('objective', models.CharField(max_length=50)),
                ('theme', models.CharField(max_length=50)),
                ('branches', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('donnee', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbWrong', models.IntegerField()),
                ('nbRight', models.IntegerField()),
                ('idExercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mathematorApp.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSimpleOperation',
            fields=[
                ('exercise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mathematorApp.Exercise')),
                ('rangeMin', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rangeMax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rangeStep', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nbOperation', models.IntegerField()),
                ('operators', models.CharField(choices=[('+', 'addition'), ('-', 'soustraction'), ('/', 'division'), ('*', 'multiplication')], default='+', max_length=1)),
            ],
            bases=('mathematorApp.exercise',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=50)),
                ('isTeacher', models.BooleanField(default=False)),
                ('relationExerciseDone', models.ManyToManyField(related_name='related_to_exercisedone', through='mathematorApp.ExerciseDone', to='mathematorApp.Exercise')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idExercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromExercise', to='mathematorApp.Exercise')),
                ('idExerciseRequirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toExercise', to='mathematorApp.Exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exercisedone',
            name='idStudent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mathematorApp.Student'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='relationExerciseDone',
            field=models.ManyToManyField(related_name='related_to_exercisedone', through='mathematorApp.ExerciseDone', to='mathematorApp.Student'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='relationExerciseRequirement',
            field=models.ManyToManyField(related_name='related_to_exerciserequirement', through='mathematorApp.ExerciseRequirement', to='mathematorApp.Exercise'),
        ),
    ]
