# Generated by Django 3.1.14 on 2022-03-15 20:20

from django.db import migrations, models
import django.db.models.deletion
import task_queue.type_constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
        ('database', '0115_auto_20220223_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(blank=True, choices=[('CREATED', 'CREATED'), ('PENDING', 'PENDING'), ('RUNNING', 'RUNNING'), ('SUCCEEDED', 'SUCCEEDED'), ('FAILED', 'FAILED')], default=task_queue.type_constants.TaskStatus['CREATED'], max_length=100, null=True)),
                ('job_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recurring_interval', models.CharField(blank=True, choices=[('EVERY_MINUTE', 'EVERY_MINUTE'), ('EVERY_HOUR', 'EVERY_HOUR'), ('EVERY_DAY', 'EVERY_DAY'), ('EVERY_MONTH', 'EVERY_MONTH'), ('EVERY_QUARTER', 'EVERY_QUARTER'), ('EVERY_YEAR', 'EVERY_YEAR')], max_length=100, null=True)),
                ('recurring_details', models.JSONField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_queue_creator', to='database.userprofile')),
                ('schedule', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_queue_schedule', to='django_celery_beat.periodictask')),
            ],
        ),
    ]