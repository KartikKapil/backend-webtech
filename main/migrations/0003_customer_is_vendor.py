# Generated by Django 3.2.5 on 2022-04-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220410_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
    ]
