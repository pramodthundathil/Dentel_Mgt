# Generated by Django 3.2.14 on 2023-01-23 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorlist',
            name='Doctirid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
