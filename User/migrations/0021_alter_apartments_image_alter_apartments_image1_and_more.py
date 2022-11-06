# Generated by Django 4.1.1 on 2022-10-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0020_apartments_aprtdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='image',
            field=models.FileField(upload_to='images/Apartment'),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='image1',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Apartment'),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='image2',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Apartment'),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='image3',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Apartment'),
        ),
    ]
