# Generated by Django 3.2.7 on 2021-09-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_auto_20210912_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
