# Generated by Django 4.2.3 on 2023-08-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Order Placed', max_length=100),
        ),
    ]