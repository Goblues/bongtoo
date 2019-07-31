# Generated by Django 2.2.3 on 2019-07-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20190730_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='activity',
            field=models.ManyToManyField(blank=True, null=True, related_name='reivews', to='commons.Activity'),
        ),
        migrations.AlterField(
            model_name='review',
            name='target',
            field=models.ManyToManyField(blank=True, null=True, related_name='reivews', to='commons.Target'),
        ),
    ]
