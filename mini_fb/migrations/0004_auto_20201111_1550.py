# Generated by Django 3.1.2 on 2020-11-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0003_profile_img_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='img_file',
        ),
        migrations.AddField(
            model_name='statusmessage',
            name='img_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
