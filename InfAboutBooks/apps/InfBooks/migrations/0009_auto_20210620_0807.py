# Generated by Django 3.2.4 on 2021-06-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfBooks', '0008_alter_book_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(to='InfBooks.Book'),
        ),
    ]
