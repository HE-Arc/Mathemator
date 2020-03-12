# Generated by Django 3.0.2 on 2020-03-12 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mathematorApp', '0006_auto_20200301_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseFixDonneeResultat',
            fields=[
                ('exercise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mathematorApp.Exercise')),
                ('result', models.CharField(default='', max_length=50)),
            ],
            bases=('mathematorApp.exercise',),
        ),
    ]