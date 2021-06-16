# Generated by Django 3.2.4 on 2021-06-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfBooks', '0003_auto_20210616_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_issue',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_return',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата книги'),
        ),
    ]
