# Generated by Django 3.2.9 on 2021-11-25 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FormPage', '0007_auto_20211125_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfiles',
            name='form_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FormPage.form'),
        ),
    ]
