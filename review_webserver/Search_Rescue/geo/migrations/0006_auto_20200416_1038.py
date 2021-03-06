# Generated by Django 3.0.3 on 2020-04-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0005_geostoremodel_geoworkspacemodel_layermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoworkspacemodel',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='geoworkspacemodel',
            name='is_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='layermodel',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
