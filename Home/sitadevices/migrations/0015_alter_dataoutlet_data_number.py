# Generated by Django 4.0.1 on 2022-04-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitadevices', '0014_dataoutlet_data_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataoutlet',
            name='data_number',
            field=models.IntegerField(default=1),
        ),
    ]
