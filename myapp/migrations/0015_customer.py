# Generated by Django 3.2.15 on 2023-08-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_delete_userr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=100)),
                ('upassword', models.CharField(max_length=100)),
                ('upharmacy_name', models.CharField(max_length=200)),
                ('ucity', models.CharField(max_length=100)),
                ('uaddress', models.CharField(max_length=200)),
                ('uemail', models.EmailField(max_length=254)),
                ('umobile_number', models.CharField(max_length=20)),
            ],
        ),
    ]
