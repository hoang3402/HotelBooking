# Generated by Django 5.0.3 on 2024-03-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_province_city_city_province_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Pending'),
        ),
    ]
