# Generated by Django 5.0.3 on 2024-03-18 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_remove_review_hotel_review_booking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.hotel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Pending'),
        ),
    ]
