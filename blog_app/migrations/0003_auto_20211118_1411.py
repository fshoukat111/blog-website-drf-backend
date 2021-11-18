# Generated by Django 3.2.8 on 2021-11-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20211118_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='category',
        ),
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='blog_app.Categories'),
        ),
    ]
