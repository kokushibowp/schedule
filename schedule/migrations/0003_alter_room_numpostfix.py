# Generated by Django 5.1.4 on 2025-04-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_rename_time1_lesson_endtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='numpostfix',
            field=models.CharField(blank=True, default='', max_length=5),
        ),
    ]
