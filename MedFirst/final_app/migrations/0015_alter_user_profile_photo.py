# Generated by Django 3.2 on 2023-07-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0014_alter_user_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='photo',
            field=models.ImageField(default='profile_phots/default.jpg', upload_to='profile_photos'),
        ),
    ]
