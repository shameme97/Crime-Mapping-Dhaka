# Generated by Django 3.2.5 on 2021-07-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_crimeincident'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeIncident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
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
    ]
