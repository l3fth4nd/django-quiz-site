# Generated by Django 2.2 on 2020-07-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(related_name='quiz', to='exam.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('answer_one', models.CharField(max_length=200)),
                ('answer_two', models.CharField(max_length=200)),
                ('answer_three', models.CharField(max_length=200)),
                ('answer_four', models.CharField(max_length=200)),
                ('answer_true', models.IntegerField(choices=[(1, 'یک'), (2, 'دو'), (3, 'سه'), (4, 'چهار')])),
                ('status', models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیشنویس')], max_length=1)),
                ('quiz', models.ManyToManyField(related_name='question', to='exam.Quiz')),
            ],
        ),
    ]
