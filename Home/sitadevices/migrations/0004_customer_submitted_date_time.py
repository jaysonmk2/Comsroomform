# Generated by Django 4.0.1 on 2022-03-28 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sitadevices', '0003_customer_remove_switch_vlan_delete_port_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='submitted_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
