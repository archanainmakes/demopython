# Generated by Django 3.2.16 on 2023-01-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('name1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='gallery')),
                ('desc1', models.TextField()),
            ],
        ),
    ]
