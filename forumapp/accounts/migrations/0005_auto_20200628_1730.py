# Generated by Django 2.1.7 on 2020-06-28 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200628_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='friends',
            new_name='follows',
        ),
    ]
