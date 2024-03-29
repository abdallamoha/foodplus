# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-04 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodplusapp', '0003_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('total', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Cooking'), (2, 'Ready'), (3, 'On the way'), (4, 'Delivered')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('picked_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplusapp.Customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplusapp.Driver')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplusapp.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplusapp.Meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='foodplusapp.Order')),
            ],
        ),
    ]
