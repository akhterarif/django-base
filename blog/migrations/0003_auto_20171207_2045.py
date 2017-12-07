# Generated by Django 2.0 on 2017-12-07 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171207_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, help_text='Deleted Time', null=True, verbose_name='DateTime Deleted'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, help_text='Category Name.', max_length=128, verbose_name='Category Name'),
            preserve_default=False,
        ),
    ]
