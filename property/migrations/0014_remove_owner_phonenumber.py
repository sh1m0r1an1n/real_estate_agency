# Generated by Django 2.2.24 on 2025-03-21 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20250321_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='phonenumber',
        ),
    ]
