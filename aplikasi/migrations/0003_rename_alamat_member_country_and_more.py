# Generated by Django 5.0 on 2023-12-31 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi', '0002_member_delete_aplikasi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='alamat',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='namabelakang',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='namadepan',
            new_name='lastname',
        ),
    ]
