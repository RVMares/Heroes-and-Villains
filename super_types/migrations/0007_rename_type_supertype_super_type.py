# Generated by Django 4.1.3 on 2022-12-11 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0006_rename_supers_type_supertype_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supertype',
            old_name='type',
            new_name='super_type',
        ),
    ]