# Generated by Django 5.2 on 2025-04-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]
