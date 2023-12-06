# Generated by Django 4.2.2 on 2023-12-06 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True, null=True)),
                ('link', models.TextField(null=True)),
                ('company', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Global', models.BooleanField(default=True)),
                ('CBC', models.BooleanField(default=True)),
                ('BBC', models.BooleanField(default=True)),
                ('Yahoo', models.BooleanField(default=True)),
                ('Google', models.BooleanField(default=True)),
                ('NPR', models.BooleanField(default=True)),
                ('Time', models.BooleanField(default=True)),
                ('Atlantic', models.BooleanField(default=True)),
                ('VOX', models.BooleanField(default=True)),
                ('ESPN', models.BooleanField(default=True)),
                ('Forbes', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
