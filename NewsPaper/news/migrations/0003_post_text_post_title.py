# Generated by Django 4.1 on 2022-09-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_author_category_comment_post_postcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
