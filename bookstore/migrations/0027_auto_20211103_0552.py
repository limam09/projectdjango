# Generated by Django 3.2.7 on 2021-11-03 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0026_auto_20211103_0529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='order',
        ),
        migrations.AddField(
            model_name='notification',
            name='to_user',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='auth.user'),
            preserve_default=False,
        ),
    ]
