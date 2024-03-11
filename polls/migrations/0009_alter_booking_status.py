# Generated by Django 5.0.3 on 2024-03-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_remove_city_country_alter_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Pending', 'Pending'), ('Completed', 'Completed'), ('Confirmed', 'Confirmed')], default='Pending'),
        ),
    ]