# Generated by Django 2.0.2 on 2018-02-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='founded_date',
            field=models.DateField(blank=True, verbose_name='date founded'),
        ),
    ]
