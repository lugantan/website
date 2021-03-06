# Generated by Django 3.1.4 on 2021-01-15 15:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0193_auto_20210101_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='additional_sponsors',
            field=models.TextField(blank=True, help_text='Outreachy needs to carefully allocate our funds. We want to try to find your community additional sponsors, so that we can fund more interns each round. Please let us know if there are organizations we could contact on your behalf for additional sponsorship.', max_length=3000, verbose_name='What other companies or organizations could Outreachy ask for additional sponsorship?'),
        ),
        migrations.AddField(
            model_name='community',
            name='general_funding_application',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='What humanitarian issues is your community addressing?'),
        ),
        migrations.AddField(
            model_name='community',
            name='humanitarian_community',
            field=models.BooleanField(default=False, verbose_name='Is your community a humanitarian open source community?'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='reason_for_participation',
            field=models.TextField(blank=True, max_length=3000, verbose_name='(Optional) Why does your community want to work with Outreachy?'),
        ),
    ]
