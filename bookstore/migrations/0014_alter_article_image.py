# Generated by Django 3.2.7 on 2021-11-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0013_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.CharField(max_length=50000),
        ),
    ]
