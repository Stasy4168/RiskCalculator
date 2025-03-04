# Generated by Django 5.1.5 on 2025-03-02 01:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0005_remove_assetsmodel_total_i'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetsmodel',
            name='corporate_floater',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Корпоративные флоатеры'),
        ),
        migrations.AlterField(
            model_name='assetsmodel',
            name='gold',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Золото'),
        ),
        migrations.AlterField(
            model_name='assetsmodel',
            name='growth_stock',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Акции роста'),
        ),
        migrations.AlterField(
            model_name='assetsmodel',
            name='state_bond',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='ОФЗ'),
        ),
    ]
