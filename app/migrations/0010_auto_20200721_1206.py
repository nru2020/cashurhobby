# Generated by Django 3.0.5 on 2020-07-21 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200720_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='cat_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]