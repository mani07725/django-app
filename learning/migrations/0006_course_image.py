# Generated by Django 4.2.1 on 2023-06-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_trainerinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='course/images'),
        ),
    ]
