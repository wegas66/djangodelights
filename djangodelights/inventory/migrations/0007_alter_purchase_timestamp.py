# Generated by Django 4.0.2 on 2022-02-09 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_purchase_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 18, 40, 35, 853941)),
        ),
    ]