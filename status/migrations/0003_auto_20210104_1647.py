# Generated by Django 2.2 on 2021-01-04 16:47

from django.db import migrations, models
import status.models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20210104_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=status.models.status_image),
        ),
    ]