# Generated by Django 4.0.1 on 2022-04-07 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitadevices', '0012_switch'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataOutlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patch_panel', models.IntegerField()),
                ('port_status', models.CharField(choices=[('ACTIVE', 'active'), ('DOWN', 'down')], max_length=200)),
                ('comroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitadevices.commmunicationroom')),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitadevices.connections')),
            ],
        ),
    ]