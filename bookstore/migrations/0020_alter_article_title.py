# Generated by Django 3.2.7 on 2021-11-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0019_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]