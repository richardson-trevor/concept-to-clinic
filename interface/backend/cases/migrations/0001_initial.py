# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 00:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('probability_concerning', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='images.ImageSeries')),
            ],
        ),
        migrations.CreateModel(
            name='Nodule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('candidate', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.Candidate')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodules', to='cases.Case')),
                ('centroid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='images.ImageLocation')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='cases.Case'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='centroid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='images.ImageLocation'),
        ),
    ]
