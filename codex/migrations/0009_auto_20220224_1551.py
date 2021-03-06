# Generated by Django 3.2 on 2022-02-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0008_item_permanent'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='charm_penalty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='coding_penalty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='endurance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='endurance_penalty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='energy_penalty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='intellect_penalty',
            field=models.IntegerField(default=0),
        ),
    ]
