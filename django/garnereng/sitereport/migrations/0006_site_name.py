# Generated by Django 2.1.3 on 2018-11-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitereport', '0005_auto_20181111_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]
