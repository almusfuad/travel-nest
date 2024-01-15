# Generated by Django 5.0.1 on 2024-01-14 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '__first__'),
        ('student', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField(blank=True, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('checkout', models.BooleanField(default=False)),
                ('booking_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='student.studentinformation')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel.hotel')),
            ],
        ),
    ]