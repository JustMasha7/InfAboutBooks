# Generated by Django 3.2.4 on 2021-06-18 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InfBooks', '0006_auto_20210618_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book',
            new_name='authors',
        ),
    ]
