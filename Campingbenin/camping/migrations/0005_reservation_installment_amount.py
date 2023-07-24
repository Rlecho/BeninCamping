# Generated by Django 4.1.7 on 2023-07-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0004_reservation_payment_status'),
    ]

    operations = [
    migrations.AddField(
        model_name='reservation',
        name='installment_amount',
        field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
    ),
]
