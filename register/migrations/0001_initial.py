# Generated by Django 3.2.8 on 2021-10-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bsc_address', models.CharField(max_length=200)),
                ('nami_address', models.CharField(max_length=200, null=True)),
                ('register_date', models.DateTimeField(verbose_name='date registered')),
            ],
        ),
    ]
