# Generated by Django 4.0.5 on 2022-06-30 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='calendar',
            new_name='categoria',
        ),
    ]