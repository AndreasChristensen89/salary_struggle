# Generated by Django 3.2 on 2022-03-11 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('char_intellect', models.IntegerField()),
                ('char_charm', models.IntegerField()),
                ('char_coding', models.IntegerField()),
                ('char_endurance', models.IntegerField()),
                ('char_money', models.IntegerField()),
                ('char_day', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Leaderboard',
            },
        ),
    ]
