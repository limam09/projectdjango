# Generated by Django 3.2.7 on 2021-11-01 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0014_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
