# Generated by Django 2.2 on 2020-07-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20200727_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='وضعیت انتشار'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='status',
            field=models.BooleanField(default=True, verbose_name='وضعیت انتشار'),
        ),
    ]