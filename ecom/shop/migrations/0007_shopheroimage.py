# Generated by Django 3.1.7 on 2021-04-12 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopheroImage',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('shopheroimage', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
