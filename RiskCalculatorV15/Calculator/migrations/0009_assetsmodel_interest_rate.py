# Generated by Django 5.1.5 on 2025-03-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0008_remove_assetsmodel_total_i'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetsmodel',
            name='interest_rate',
            field=models.FloatField(default=21),
        ),
    ]
