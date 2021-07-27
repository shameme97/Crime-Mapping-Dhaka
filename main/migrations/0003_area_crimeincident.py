# Generated by Django 3.2.5 on 2021-07-27 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20210727_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeIncident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=150)),
                ('nature_of_crime', models.CharField(max_length=50)),
                ('report_status', models.BooleanField()),
                ('report_id', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('date_of_crime', models.DateField()),
                ('time_of_crime', models.TimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number_of_crimes', models.IntegerField()),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.crimeincident')),
            ],
        ),
    ]
