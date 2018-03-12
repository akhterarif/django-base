# Generated by Django 2.0 on 2018-03-12 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180307_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Select a Category Name.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_model_category', to='blog.CategoryModel', verbose_name='Category'),
        ),
    ]