# Generated by Django 5.0.4 on 2024-04-28 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0015_aboutcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlyAskedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('section', models.IntegerField()),
                ('sub_section', models.IntegerField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='aboutcontent',
            name='title_one',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='aboutcontent',
            name='title_three',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='aboutcontent',
            name='title_two',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='buyers_budget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyers_profile', to='promo.budgetrange'),
        ),
        migrations.AddField(
            model_name='profile',
            name='interested_consignments',
            field=models.ManyToManyField(related_name='sellers_profiles', to='promo.service'),
        ),
        migrations.AddField(
            model_name='profile',
            name='interested_services',
            field=models.ManyToManyField(related_name='buyers_profiles', to='promo.service'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_buyer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='sellers_budget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sellers_profile', to='promo.budgetrange'),
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
