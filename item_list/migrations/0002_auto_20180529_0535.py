# Generated by Django 2.0.5 on 2018-05-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
