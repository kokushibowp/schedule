# Generated by Django 5.1.4 on 2025-04-07 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_id',
            new_name='id',
        ),
    ]
