# Generated by Django 2.2.12 on 2022-01-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0002_sidebar_edit_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='First_page_edit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='First_page_edit')),
            ],
        ),
    ]