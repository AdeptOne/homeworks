# Generated by Django 3.1.2 on 2022-05-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=False, verbose_name='LTE')),
                ('slug', models.SlugField()),
            ],
        ),
    ]