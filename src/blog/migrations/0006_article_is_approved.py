# Generated by Django 2.0.6 on 2018-07-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
