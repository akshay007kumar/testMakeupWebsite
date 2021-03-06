# Generated by Django 2.2.1 on 2020-08-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200803_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='MakeupOffers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now_add=True)),
                ('message', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Makeup Offers',
            },
        ),
    ]
