# Generated by Django 4.2.6 on 2023-10-26 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='jop_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='', max_length=104),
            preserve_default=False,
        ),
    ]
