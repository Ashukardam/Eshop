# Generated by Django 4.2.1 on 2023-07-16 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutproducts',
            old_name='Checkout',
            new_name='checkout',
        ),
    ]