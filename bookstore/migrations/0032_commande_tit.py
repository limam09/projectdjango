# Generated by Django 3.2.7 on 2021-11-05 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0031_remove_commande_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='tit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookstore.article'),
            preserve_default=False,
        ),
    ]
