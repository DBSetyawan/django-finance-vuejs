# Generated by Django 3.2.4 on 2021-06-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuedjango', '0004_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='myaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=500, null=True)),
                ('product_name', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.FloatField(blank=True, max_length=500, null=True)),
                ('price', models.FloatField(blank=True, max_length=500, null=True)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
    ]
