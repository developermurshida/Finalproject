# Generated by Django 4.2.15 on 2024-09-01 19:03

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
                ('title', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=4)),
            ],
        ),
    ]
