# Generated by Django 5.0.4 on 2024-04-06 19:54

import promo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0003_legendvideo_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompareSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_one', models.ImageField(upload_to=promo.models.CompareSlider.slider_directory_path)),
                ('title_one', models.CharField(max_length=100)),
                ('info_one', models.TextField()),
                ('image_two', models.ImageField(upload_to=promo.models.CompareSlider.slider_directory_path)),
                ('title_two', models.CharField(max_length=100)),
                ('info_two', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='legendvideo',
            name='info',
            field=models.TextField(default='This is some default text'),
            preserve_default=False,
        ),
    ]
