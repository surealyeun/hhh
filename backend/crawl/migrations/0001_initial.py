# Generated by Django 2.2.5 on 2020-04-28 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0016_auto_20200421_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrctSense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftype', models.CharField(max_length=10)),
                ('word', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('district', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StoreSense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftype', models.CharField(max_length=10)),
                ('word', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DiningStore', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='StoreImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.TextField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DiningStore')),
            ],
        ),
        migrations.CreateModel(
            name='LocationSense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftype', models.CharField(max_length=10)),
                ('word', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Location', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='LocationImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Location')),
            ],
        ),
    ]
