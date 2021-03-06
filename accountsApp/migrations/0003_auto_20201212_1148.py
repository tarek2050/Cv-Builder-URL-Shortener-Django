# Generated by Django 3.1.2 on 2020-12-12 10:48

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accountsApp', '0002_auto_20201211_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=75, size=[300, 300], upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='profile',
            name='toppings',
            field=models.ManyToManyField(blank=True, null=True, to='accountsApp.Topping'),
        ),
    ]
