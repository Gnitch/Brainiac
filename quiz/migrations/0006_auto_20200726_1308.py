# Generated by Django 3.0.3 on 2020-07-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_studentquizinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentquizinfo',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
