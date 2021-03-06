# Generated by Django 4.0.4 on 2022-05-30 02:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='hate_users',
            field=models.ManyToManyField(related_name='hate_ingredients', through='accounts.Hate_Ingredient', to=settings.AUTH_USER_MODEL),
        ),
    ]
