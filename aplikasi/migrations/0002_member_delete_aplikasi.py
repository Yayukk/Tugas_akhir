# Generated by Django 5.0 on 2023-12-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namadepan', models.CharField(max_length=100)),
                ('namabelakang', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Aplikasi',
        ),
    ]