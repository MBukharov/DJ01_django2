# Generated by Django 5.1.3 on 2024-11-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='author',
            new_name='source'
        ),
    ]
