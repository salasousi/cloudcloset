# Generated by Django 4.1.6 on 2023-02-10 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_style_alter_outfit_name_remove_outfit_occasion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outfit',
            old_name='occasion',
            new_name='style',
        ),
    ]
