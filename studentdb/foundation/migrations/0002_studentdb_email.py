# Generated by Django 2.2.7 on 2019-11-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdb',
            name='email',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]
