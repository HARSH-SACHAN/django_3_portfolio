# Generated by Django 3.1 on 2020-09-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info', '0002_auto_20200906_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]