# Generated by Django 3.2.22 on 2023-12-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps__campaigns', '0022_campaigncommunity_help_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigntechnologylike',
            name='community_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]