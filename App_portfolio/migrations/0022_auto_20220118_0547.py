# Generated by Django 2.2.12 on 2022-01-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0021_remove_myproject_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprojects_update',
            name='Project_Link',
            field=models.CharField(max_length=150),
        ),
    ]
