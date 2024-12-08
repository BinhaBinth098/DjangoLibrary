# Generated by Django 3.2.25 on 2024-10-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emid', models.IntegerField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]