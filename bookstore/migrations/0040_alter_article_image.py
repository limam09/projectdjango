# Generated by Django 3.2.7 on 2021-11-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0039_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]