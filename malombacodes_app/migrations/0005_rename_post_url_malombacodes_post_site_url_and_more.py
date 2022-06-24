# Generated by Django 4.0.5 on 2022-06-24 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malombacodes_app', '0004_alter_malombacodes_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='malombacodes_post',
            old_name='post_url',
            new_name='site_url',
        ),
        migrations.AddField(
            model_name='malombacodes_post',
            name='notes',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='malombacodes_post',
            name='site_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='malombacodes_post',
            name='youtube_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='malombacodes_post',
            name='post_description',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
