# Generated by Django 4.2.3 on 2023-07-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='total_client',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='won',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='year',
            field=models.PositiveIntegerField(default=1),
        ),
    ]