# Generated by Django 3.2.9 on 2021-11-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormPage', '0011_alter_form_agreed_to_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='agreed_to_terms',
            field=models.BooleanField(default=False),
        ),
    ]
