# Generated by Django 5.0 on 2023-12-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0004_alter_yangilikklar_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
