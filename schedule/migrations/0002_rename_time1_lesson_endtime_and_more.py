# Generated by Django 5.1.4 on 2025-04-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='time1',
            new_name='endTime',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='teachername',
            new_name='lecturer',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='time2',
            new_name='startTime',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='discipline',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='numclassroom',
            new_name='roomNumber',
        ),
        migrations.AlterField(
            model_name='room',
            name='NFC',
            field=models.CharField(default='none', max_length=50, unique=True),
        ),
    ]
