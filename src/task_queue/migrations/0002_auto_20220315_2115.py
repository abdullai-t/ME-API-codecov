# Generated by Django 3.1.14 on 2022-03-15 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_queue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='recurring_interval',
            field=models.CharField(blank=True, choices=[('EVERY_MINUTE', 'EVERY_MINUTE'), ('EVERY_HOUR', 'EVERY_HOUR'), ('EVERY_DAY', 'EVERY_DAY'), ('EVERY_MONTH', 'EVERY_MONTH'), ('EVERY_QUARTER', 'EVERY_QUARTER'), ('EVERY_YEAR', 'EVERY_YEAR'), ('ONE_OFF', 'ONE_OFF')], max_length=100, null=True),
        ),
    ]