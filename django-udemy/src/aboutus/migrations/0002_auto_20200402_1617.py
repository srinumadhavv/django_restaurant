# Generated by Django 2.2 on 2020-04-02 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About Us', 'verbose_name_plural': 'About us'},
        ),
        migrations.AlterModelOptions(
            name='chef',
            options={'verbose_name': 'chef', 'verbose_name_plural': 'chef'},
        ),
        migrations.AlterModelOptions(
            name='why_choose_us',
            options={'verbose_name': 'why choose us', 'verbose_name_plural': 'why choose us'},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
    ]
