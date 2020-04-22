# Generated by Django 3.0.3 on 2020-04-16 07:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200415_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskusermodel',
            name='coverage_id',
        ),
        migrations.AlterField(
            model_name='caseoilinfo',
            name='forecast_date',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='caserescueinfo',
            name='forecast_date',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='taskusermodel',
            name='forecast_date',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]
