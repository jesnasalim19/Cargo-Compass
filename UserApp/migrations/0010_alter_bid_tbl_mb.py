# Generated by Django 4.2.7 on 2024-03-28 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0009_alter_bid_tbl_et_alter_bid_tbl_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid_tbl',
            name='mb',
            field=models.CharField(max_length=25),
        ),
    ]
