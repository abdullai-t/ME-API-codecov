# Generated by Django 3.1.12 on 2021-08-13 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0094_auto_20210724_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='attained_carbon_footprint_reduction',
            new_name='initial_carbon_footprint_reduction',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='attained_number_of_actions',
            new_name='initial_number_of_actions',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='attained_number_of_households',
            new_name='initial_number_of_households',
        ),
    ]