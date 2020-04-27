# Generated by Django 3.0.3 on 2020-04-16 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0009_rgeoinfo_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='rgeoinfo',
            name='coverage',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='geo.CoverageModel'),
        ),
    ]