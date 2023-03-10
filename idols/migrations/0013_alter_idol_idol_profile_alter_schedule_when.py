# Generated by Django 4.1.7 on 2023-03-10 04:52

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0012_alter_idol_idol_anniv_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idol',
            name='idol_profile',
            field=models.URLField(blank=True, max_length=10000, null=True, validators=[django.core.validators.URLValidator('유효한 URL을 입력하세요. ')]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 4, 52, 0, 131525, tzinfo=datetime.timezone.utc)),
        ),
    ]
