# Generated by Django 2.1.1 on 2020-03-27 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_meals_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meals',
            options={'verbose_name': 'meal', 'verbose_name_plural': 'meals'},
        ),
    ]
