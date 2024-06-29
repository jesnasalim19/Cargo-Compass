# Generated by Django 4.2.7 on 2024-03-05 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comp_det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro', models.CharField(max_length=25)),
                ('pic', models.FileField(upload_to='pictures')),
                ('prc', models.IntegerField()),
                ('des', models.TextField()),
                ('cnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProApp.pro_comp')),
            ],
        ),
    ]