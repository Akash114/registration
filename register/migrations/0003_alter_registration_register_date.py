# Generated by Django 3.2.8 on 2021-11-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_registration_nami_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date registered'),
        ),
    ]
