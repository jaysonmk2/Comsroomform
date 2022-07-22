# Generated by Django 4.0.6 on 2022-07-21 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sitadevices', '0002_alter_connections_data_outlet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connections',
            name='disconnection_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
