# Generated by Django 4.1.13 on 2024-05-17 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0019_alter_folders_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 17, 12, 9, 39, 710914, tzinfo=datetime.timezone.utc)),
        ),
    ]
