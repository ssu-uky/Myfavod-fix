# Generated by Django 4.1.7 on 2023-03-05 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0005_schedule_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='type',
        ),
    ]