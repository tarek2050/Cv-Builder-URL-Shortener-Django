# Generated by Django 3.1.2 on 2020-12-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsApp', '0007_auto_20201212_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', height_field='250', upload_to='profile_pics', width_field='250'),
        ),
    ]
