# Generated by Django 4.2.2 on 2023-06-13 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='id')),
                ('descri', models.TextField()),
            ],
        ),
    ]
