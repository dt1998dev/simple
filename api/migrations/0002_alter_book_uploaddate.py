# Generated by Django 3.2.5 on 2022-09-11 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uploadDate',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
