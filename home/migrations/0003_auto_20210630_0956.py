# Generated by Django 3.1.12 on 2021-06-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_about_me_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='call_me',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='email_me',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='open_hours',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
