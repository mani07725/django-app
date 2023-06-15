# Generated by Django 4.2.1 on 2023-06-10 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='description',
            field=models.TextField(default=None, null=True),
        ),
        migrations.CreateModel(
            name='Trainerinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('Trainerinfo', models.TextField(blank=True, null=True)),
                ('Trinerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.trainer')),
            ],
        ),
    ]
