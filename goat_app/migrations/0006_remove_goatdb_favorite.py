# Generated by Django 2.2 on 2021-09-15 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goat_app', '0005_auto_20210915_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goatdb',
            name='favorite',
        ),
    ]