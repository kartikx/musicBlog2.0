# Generated by Django 3.0.8 on 2020-08-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mBlogApp', '0011_post_upvotedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='albumart',
            field=models.ImageField(blank=True, default='defaultalbumart.jpg', null=True, upload_to='album_art'),
        ),
    ]
