# Generated by Django 3.2.7 on 2021-11-02 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0024_commande_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='Article',
        ),
    ]
