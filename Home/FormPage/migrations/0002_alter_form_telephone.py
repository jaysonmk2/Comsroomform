# Generated by Django 3.2.9 on 2021-11-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]
