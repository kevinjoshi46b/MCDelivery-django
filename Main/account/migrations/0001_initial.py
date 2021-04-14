# Generated by Django 3.2 on 2021-04-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20210414_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('user_cart', models.ManyToManyField(null=True, to='products.Food')),
            ],
        ),
    ]