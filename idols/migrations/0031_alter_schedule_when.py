# Generated by Django 4.1.7 on 2023-03-10 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0030_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]