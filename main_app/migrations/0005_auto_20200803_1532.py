# Generated by Django 2.2.1 on 2020-08-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_makeupoffers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeupoffers',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='makeupoffers',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]