# Generated by Django 3.2 on 2022-02-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0003_rename_endurance_item_energy'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
