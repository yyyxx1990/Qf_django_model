# Generated by Django 3.2.13 on 2025-05-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_num', models.CharField(max_length=16, unique=True)),
                ('o_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
