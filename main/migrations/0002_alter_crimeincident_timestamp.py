# Generated by Django 3.2.5 on 2021-07-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimeincident',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
