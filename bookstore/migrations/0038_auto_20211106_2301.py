# Generated by Django 3.2.7 on 2021-11-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0037_auto_20211106_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='desc_ar',
            new_name='desc_fr',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title_ar',
        ),
        migrations.AddField(
            model_name='article',
            name='title_fr',
            field=models.CharField(default=6, max_length=50),
            preserve_default=False,
        ),
    ]
