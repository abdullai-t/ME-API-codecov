# Generated by Django 3.1.14 on 2022-12-14 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0124_userprofile_notification_dates'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='action',
            unique_together=set(),
        ),
    ]