# Generated by Django 3.2.22 on 2024-02-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_buyproduct_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyproduct',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
