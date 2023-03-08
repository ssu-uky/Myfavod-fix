# Generated by Django 4.1.7 on 2023-03-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('broadcast', 'BROADCASTS'), ('event', 'EVENTS'), ('release', 'RELEASES'), ('congrats', 'CONGRATS'), ('sns', 'SNS'), ('etc', 'ETC')], default='', max_length=15)),
                ('content', models.TextField(default='', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
