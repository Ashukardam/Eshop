# Generated by Django 4.2.1 on 2023-06-29 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_buyer_addressline1_alter_buyer_addressline2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='city',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pin',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='state',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
