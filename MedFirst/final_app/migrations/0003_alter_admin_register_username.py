# Generated by Django 3.2 on 2021-05-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0002_auto_20210503_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_register',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
