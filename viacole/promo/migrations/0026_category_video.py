# Generated by Django 5.0.4 on 2024-05-06 10:43

import django.core.validators
import promo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0025_category_service_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=promo.models.Category.category_upload, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'avi', 'mkv'])]),
        ),
    ]
