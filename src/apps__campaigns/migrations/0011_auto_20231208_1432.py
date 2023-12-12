# Generated by Django 3.1.14 on 2023-12-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps__campaigns', '0010_campaign_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='community',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='deal_section',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='more_details',
            field=models.JSONField(blank=True, null=True),
        ),
    ]