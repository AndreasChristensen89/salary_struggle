# Generated by Django 3.2 on 2022-03-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0009_auto_20220224_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewer',
            name='intro',
            field=models.TextField(default=''),
        ),
    ]
