# Generated by Django 4.0.2 on 2022-02-10 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_remove_purchase_timestamp_purchase_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='time',
            field=models.TimeField(default=datetime.time(0, 46, 44, 321233)),
        ),
    ]