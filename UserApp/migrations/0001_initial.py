# Generated by Django 4.2.7 on 2024-03-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fnm', models.CharField(max_length=25)),
                ('mob', models.IntegerField()),
                ('eml', models.EmailField(max_length=254)),
                ('psw', models.CharField(max_length=25)),
                ('cpsw', models.CharField(max_length=25)),
            ],
        ),
    ]
