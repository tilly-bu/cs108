# Generated by Django 3.1.2 on 2020-11-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0004_auto_20201111_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='_profile_friends_+', to='mini_fb.Profile'),
        ),
    ]