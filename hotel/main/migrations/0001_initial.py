# Generated by Django 4.2.13 on 2024-06-26 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=256)),
                ('hotel_price', models.IntegerField()),
                ('banner_image', models.ImageField(upload_to='media/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_At', models.DateField(auto_now=True)),
                ('description', models.TextField()),
                ('amenities', models.ManyToManyField(to='main.amenities')),
            ],
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_At', models.DateField(auto_now=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel')),
            ],
        ),
    ]
