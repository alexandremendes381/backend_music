# Generated by Django 4.2.3 on 2023-07-15 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postspage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postsmodel',
            old_name='imagem',
            new_name='arquivo',
        ),
    ]