# Generated by Django 3.2.7 on 2021-09-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_customer_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, default='person.png', null=True, upload_to=''),
        ),
    ]