# Generated by Django 3.1.4 on 2021-02-05 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210131_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.TextField(max_length=250, verbose_name='details'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name='rating'),
        ),
    ]