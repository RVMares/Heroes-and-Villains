# Generated by Django 4.1.3 on 2022-12-10 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0004_rename_type_supertype_super_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supertype',
            old_name='super_type',
            new_name='supers_type',
        ),
    ]