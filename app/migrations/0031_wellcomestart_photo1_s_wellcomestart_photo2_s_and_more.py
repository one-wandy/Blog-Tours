# Generated by Django 4.2 on 2023-05-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_wellcomestart'),
    ]

    operations = [
        migrations.AddField(
            model_name='wellcomestart',
            name='photo1_s',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='wellcomestart',
            name='photo2_s',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='wellcomestart',
            name='photo3_s',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='wellcomestart',
            name='photo4_s',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
