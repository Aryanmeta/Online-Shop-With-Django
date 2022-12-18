# Generated by Django 4.1.3 on 2022-12-18 09:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_short_description_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Comment Display'),
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(blank=True, default=True, verbose_name='Product Display'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Product Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=300, verbose_name='Product Short Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Product Title'),
        ),
    ]
