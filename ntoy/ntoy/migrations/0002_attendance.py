# Generated by Django 3.1.3 on 2022-09-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntoy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('attendance', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
    ]
