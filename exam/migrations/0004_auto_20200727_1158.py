# Generated by Django 2.2 on 2020-07-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20200727_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='quiz', to='exam.Category', verbose_name='دسته بندی'),
        ),
    ]