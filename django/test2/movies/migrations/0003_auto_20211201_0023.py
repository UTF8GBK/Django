# Generated by Django 2.2 on 2021-11-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]