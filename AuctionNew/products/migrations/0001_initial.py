# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BidPrice', models.IntegerField()),
                ('By', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Code', models.IntegerField(null=True)),
                ('Title', models.CharField(max_length=26, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Final_price', models.IntegerField()),
                ('Sold_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterestedIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=96)),
                ('BidStart', models.IntegerField(null=True)),
                ('BidPrice', models.IntegerField(blank=True, null=True)),
                ('Photos', models.ImageField(help_text='Upload image of your Product', blank=True, upload_to='products_uploaded/')),
                ('Timer', models.TimeField()),
                ('Till', models.DateField()),
                ('On', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(max_length=1000, null=True)),
                ('By', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
                ('Category', models.ForeignKey(to='products.Category', null=True)),
                ('Followedby', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='interestedin',
            name='Items',
            field=models.ManyToManyField(to='products.Product'),
        ),
        migrations.AddField(
            model_name='interestedin',
            name='User_interested',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='history',
            name='Item',
            field=models.ForeignKey(to='products.Product'),
        ),
        migrations.AddField(
            model_name='bid',
            name='Item',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]
