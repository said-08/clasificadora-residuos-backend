# Generated by Django 5.0.3 on 2024-03-07 02:19

import waste.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waste',
            name='img',
            field=models.ImageField(default='posts/default.jpg', upload_to=waste.models.upload_to, verbose_name='Image'),
        ),
    ]
