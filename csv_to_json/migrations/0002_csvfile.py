# Generated by Django 2.2.5 on 2020-02-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_to_json', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='csvfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('iswc', models.CharField(max_length=255, unique=True)),
                ('contributer', models.CharField(max_length=255)),
            ],
        ),
    ]
