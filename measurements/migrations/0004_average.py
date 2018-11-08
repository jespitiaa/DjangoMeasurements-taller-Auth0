# Generated by Django 2.1.3 on 2018-11-08 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0003_threshold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Average',
            fields=[
                ('total', models.IntegerField()),
                ('avg', models.FloatField(blank=True, default=None, null=True)),
                ('variable', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='measurements.Variable')),
            ],
        ),
    ]
