# Generated by Django 4.2.3 on 2023-07-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.FileField(upload_to='posts/')),
                ('texto', models.CharField(max_length=500)),
            ],
        ),
    ]