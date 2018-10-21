# Generated by Django 2.1.1 on 2018-10-21 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20181021_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='bachelor',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='family',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='girls',
        ),
        migrations.AddField(
            model_name='preference',
            name='preference',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='bhk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search.Bhk'),
        ),
        migrations.RemoveField(
            model_name='property',
            name='preference',
        ),
        migrations.AddField(
            model_name='property',
            name='preference',
            field=models.ManyToManyField(to='search.Preference'),
        ),
    ]
