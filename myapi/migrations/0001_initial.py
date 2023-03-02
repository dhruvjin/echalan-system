# Generated by Django 4.1.5 on 2023-01-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('plate', models.CharField(max_length=21)),
                ('engine', models.CharField(max_length=50)),
                ('chasis', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=50)),
            ],
        ),
    ]
