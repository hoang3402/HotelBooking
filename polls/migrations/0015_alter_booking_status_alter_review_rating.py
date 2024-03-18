# Generated by Django 5.0.3 on 2024-03-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_review_hotel_alter_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Confirmed', 'Confirmed'), ('Pending', 'Pending')], default='Pending'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]