# Generated by Django 5.1.5 on 2025-03-01 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0003_delete_total_alter_assetsmodel_corporate_floater_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetsmodel',
            name='total_i',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
