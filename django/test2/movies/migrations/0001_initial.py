# Generated by Django 2.2 on 2021-10-18 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('score', models.FloatField(default=0.0)),
                ('number', models.IntegerField(default=0)),
                ('image_path', models.CharField(max_length=255)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='heroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attrs', models.CharField(max_length=20)),
                ('startdata', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('isDelete', models.BooleanField(default=False)),
                ('movies_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.moviesInfo')),
            ],
        ),
    ]