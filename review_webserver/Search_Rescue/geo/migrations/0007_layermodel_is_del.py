# Generated by Django 3.0.3 on 2020-04-16 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0006_auto_20200416_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='layermodel',
            name='is_del',
            field=models.BooleanField(default=False),
        ),
    ]