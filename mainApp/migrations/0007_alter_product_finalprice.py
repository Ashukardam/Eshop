# Generated by Django 4.2.1 on 2023-07-06 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_alter_buyer_city_alter_buyer_pin_alter_buyer_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='finalprice',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
