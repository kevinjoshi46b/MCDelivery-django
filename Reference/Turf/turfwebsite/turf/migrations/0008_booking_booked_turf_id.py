# Generated by Django 3.1.5 on 2021-01-26 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0007_auto_20210127_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked_turf_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='turf.turf_list'),
        ),
    ]