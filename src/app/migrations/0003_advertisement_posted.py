# Generated by Django 4.0 on 2021-12-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_advertisement_address_alter_advertisement_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]