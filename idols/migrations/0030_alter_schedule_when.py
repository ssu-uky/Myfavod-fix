# Generated by Django 4.1.7 on 2023-03-10 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0029_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 17, 20, 25, 362929, tzinfo=datetime.timezone.utc)),
        ),
    ]
