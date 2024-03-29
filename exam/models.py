from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

##MANAGER

class QuestionManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class QuizManager(models.Manager):
    def published(self):
        return self.filter(status=True)



# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان')
    slug   = models.SlugField(unique=True, verbose_name='آدرس')
    status = models.BooleanField(default=True, verbose_name='وضعیت انتشار')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['status']
    def __str__(self):
        return self.title

class Quiz(models.Model):
    title  = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.CharField(max_length=250, verbose_name='توضیحات', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1, related_name='quiz', verbose_name='نویسنده')
    category = models.ManyToManyField(Category, default=None, blank=True, related_name='quiz', verbose_name='دسته بندی')
    slug   = models.SlugField(unique=True, verbose_name='آدرس')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    status = models.BooleanField(default=True, verbose_name='وضعیت انتشار')
    class Meta:
        verbose_name = 'آزمون'
        verbose_name_plural = 'آزمون ها'
        ordering = ['-publish']
    def __str__(self):
        return self.title

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.all()])
    category_to_str.short_description = 'دسته بندی ها'

    def count_question_publish(self):
        return self.question.filter(status='p').count()
    count_question_publish.short_description = 'تعداد سوالات'

    objects = QuizManager()




class Question(models.Model):
    ANSWER_CHOICES =(
    (1,'یک'),
    (2,'دو'),
    (3,'سه'),
    (4,'چهار'),
    )
    STATUS_CHOICES=(
    ('p','منتشر شده'),
    ('d','پیشنویس'),
    )
    title = models.CharField(max_length=300, verbose_name='عنوان')
    quiz  = models.ManyToManyField(Quiz, related_name='question', verbose_name='آموزن')
    answer_one = models.CharField(max_length=300, verbose_name='گزینه یک')
    answer_two = models.CharField(max_length=300, verbose_name='گزینه دو')
    answer_three = models.CharField(max_length=300, verbose_name='گزینه سه')
    answer_four = models.CharField(max_length=300, verbose_name='گزینه چهار')
    answer_true = models.IntegerField(choices=ANSWER_CHOICES, verbose_name='گزینه صحیح')
    status = models.CharField(max_length=1, default='p', choices=STATUS_CHOICES, verbose_name='وضعیت')
    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'
        ordering = ['status']
    def __str__(self):
        return self.title

    def quiz_to_str(self):
        return "، ".join([quiz.title for quiz in self.quiz.all()])
    quiz_to_str.short_description = 'آزمون های'

    objects = QuestionManager()
