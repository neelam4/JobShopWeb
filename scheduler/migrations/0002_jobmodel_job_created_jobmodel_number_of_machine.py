# Generated by Django 4.0.3 on 2022-03-28 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='job_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='number_of_machine',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]