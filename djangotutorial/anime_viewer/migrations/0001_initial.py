# Generated by Django 5.2 on 2025-04-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anime_movie', '0002_animemovie_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeViewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateField(auto_now_add=True)),
                ('watched_anime_list', models.ManyToManyField(blank=True, related_name='viewers', to='anime_movie.animemovie')),
            ],
        ),
    ]
