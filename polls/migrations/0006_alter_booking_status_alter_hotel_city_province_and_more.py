# Generated by Django 5.0.3 on 2024-03-10 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_booking_adults_remove_booking_children_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Pending'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.city'),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.country')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.province'),
        ),
    ]