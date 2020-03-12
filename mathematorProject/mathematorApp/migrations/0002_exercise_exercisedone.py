# Generated by Django 3.0.2 on 2020-02-27 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mathematorApp', '0001_initial'),
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
            ],
        ),
        migrations.CreateModel(
            name='ExerciseDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbWrong', models.IntegerField()),
                ('nbRight', models.IntegerField()),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mathematorApp.Student')),
            ],
        ),
    ]