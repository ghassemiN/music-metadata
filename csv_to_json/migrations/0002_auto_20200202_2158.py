# Generated by Django 2.2.5 on 2020-02-02 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_to_json', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song_contributer',
            old_name='contributer_id',
            new_name='contributer',
        ),
        migrations.RenameField(
            model_name='song_contributer',
            old_name='song_id',
            new_name='song',
        ),
        migrations.AlterUniqueTogether(
            name='song_contributer',
            unique_together={('contributer', 'song')},
        ),
    ]
