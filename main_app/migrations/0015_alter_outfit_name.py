# Generated by Django 4.1.6 on 2023-02-11 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_remove_outfit_occasions_style_outfit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]