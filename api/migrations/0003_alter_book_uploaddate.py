# Generated by Django 3.2.5 on 2022-09-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_book_uploaddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uploadDate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
