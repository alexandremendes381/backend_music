# Generated by Django 4.2.3 on 2023-07-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_rename_neighborhood_cadastromodel_bairro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastromodel',
            name='selfie',
            field=models.FileField(default=2, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
