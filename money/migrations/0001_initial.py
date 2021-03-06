# Generated by Django 2.1.1 on 2018-12-17 02:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(choices=[('E', 'EXPENSE'), ('I', 'INCOME')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('note', models.CharField(max_length=250)),
                ('time', models.DateTimeField(default=datetime.datetime(2018, 12, 17, 9, 48, 9, 274383))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=250)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money.Wallet'),
        ),
    ]
