# Generated by Django 3.2 on 2022-02-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activecharacter',
            name='day',
            field=models.IntegerField(default=1),
        ),
    ]