# Generated by Django 2.1 on 2018-08-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20180707_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerinfo',
            name='confirmation_code',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
