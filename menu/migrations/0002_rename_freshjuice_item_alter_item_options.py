# Generated by Django 4.2.2 on 2023-06-29 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FreshJuice',
            new_name='Item',
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-pk'], 'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
    ]