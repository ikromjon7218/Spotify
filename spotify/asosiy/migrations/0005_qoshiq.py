# Generated by Django 4.1.5 on 2023-03-23 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0004_delete_qoshiq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qoshiq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('janr', models.CharField(max_length=100)),
                ('sana', models.DateField()),
                ('fayl', models.FileField(upload_to='')),
                ('davomiylik', models.DurationField()),
                ('albom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiy.albom')),
            ],
        ),
    ]
