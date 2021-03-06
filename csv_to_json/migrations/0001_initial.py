# Generated by Django 2.2.5 on 2020-02-03 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('iswc', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='contributers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributer', models.CharField(max_length=255)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='csv_to_json.songs')),
            ],
            options={
                'unique_together': {('contributer', 'song')},
            },
        ),
        migrations.CreateModel(
            name='song_contributer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csv_to_json.contributers')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csv_to_json.songs')),
            ],
            options={
                'unique_together': {('contributer', 'song')},
            },
        ),
    ]
