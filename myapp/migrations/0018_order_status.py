# Generated by Django 3.2.15 on 2023-08-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.TextField(default='pending'),
        ),
    ]