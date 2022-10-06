# Generated by Django 4.1.2 on 2022-10-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=150)),
                ('image_url', models.CharField(max_length=100)),
            ],
        ),
    ]