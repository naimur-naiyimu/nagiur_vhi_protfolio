# Generated by Django 4.2.4 on 2024-03-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('al_content', '0006_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(default=1, upload_to='al_content/media/'),
            preserve_default=False,
        ),
    ]
