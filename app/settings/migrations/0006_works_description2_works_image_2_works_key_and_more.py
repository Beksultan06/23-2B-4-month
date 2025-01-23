# Generated by Django 4.2.7 on 2025-01-23 12:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0005_works"),
    ]

    operations = [
        migrations.AddField(
            model_name="works",
            name="description2",
            field=ckeditor.fields.RichTextField(default=1, verbose_name="Описание"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="works",
            name="image_2",
            field=models.ImageField(default=1, upload_to="works", verbose_name="Фото"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="works",
            name="key",
            field=models.CharField(default=1, max_length=155, verbose_name="Ключ"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="works",
            name="title2",
            field=models.CharField(default=1, max_length=155, verbose_name="Заголовок"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="works",
            name="value",
            field=models.CharField(default=1, max_length=155, verbose_name="Значение"),
            preserve_default=False,
        ),
    ]
