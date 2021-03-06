# Generated by Django 3.0.3 on 2020-04-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200407_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskusermodel',
            name='coverage_area',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='taskusermodel',
            name='coverage_type',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='taskusermodel',
            name='product_type',
            field=models.IntegerField(choices=[(1, 'DAILY_CURRENT_BHS'), (2, 'DAILY_CURRENT_ECS'), (3, 'DAILY_CURRENT_IND'), (4, 'DAILY_CURRENT_SCS'), (5, 'DAILY_CURRENT_NWP'), (6, 'DAILY_WIND_WRF')], default=-1),
        ),
    ]
