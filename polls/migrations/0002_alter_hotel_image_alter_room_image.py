# Generated by Django 5.0.2 on 2024-02-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
