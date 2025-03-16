# Generated by Django 5.1.7 on 2025-03-16 14:02

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0006_flat_liked_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="flat",
            name="owner_pure_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                help_text="Формат: +7XXXXXXXXXX",
                max_length=128,
                region="RU",
                verbose_name="Нормализированный номер владельца",
            ),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="flat",
            name="has_balcony",
            field=models.BooleanField(
                blank=True, db_index=True, null=True, verbose_name="Наличие балкона"
            ),
        ),
        migrations.AlterField(
            model_name="flat",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
