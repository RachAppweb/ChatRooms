# Generated by Django 3.2 on 2023-07-29 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
