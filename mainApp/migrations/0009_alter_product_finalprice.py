# Generated by Django 4.2.1 on 2023-07-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_alter_product_finalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='finalprice',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]