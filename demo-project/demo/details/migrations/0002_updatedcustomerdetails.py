# Generated by Django 5.0.2 on 2024-03-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdatedCustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_id', models.CharField(max_length=100)),
                ('passport_id', models.CharField(max_length=100)),
            ],
        ),
    ]
