# Generated by Django 4.1.3 on 2022-12-08 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0003_rename_super_type_supertype_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supertype',
            old_name='type',
            new_name='super_type',
        ),
    ]
