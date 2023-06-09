# Generated by Django 4.1.5 on 2023-03-17 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('sana', models.DateField(blank=True, null=True)),
                ('rasm', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiqchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=40)),
                ('tugilgan_yil', models.DateField()),
                ('davlat', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('janr', models.CharField(max_length=100)),
                ('tugilgan_yil', models.DateField()),
                ('davomiylik', models.DurationField()),
                ('albom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiy.albom')),
            ],
        ),
        migrations.AddField(
            model_name='albom',
            name='qoshiqchi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.qoshiqchi'),
        ),
    ]
