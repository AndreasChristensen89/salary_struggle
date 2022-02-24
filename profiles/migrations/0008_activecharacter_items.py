# Generated by Django 3.2 on 2022-02-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0008_item_permanent'),
        ('profiles', '0007_auto_20220223_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='activecharacter',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='character_items', to='codex.Item'),
        ),
    ]
