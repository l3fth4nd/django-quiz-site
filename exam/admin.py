from django.contrib import admin
from .models import Category, Quiz, Question

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('title','slug','status')
    list_filter   = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category,CategoryAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display  = ('title', 'author','slug','status','category_to_str','publish','count_question_publish')
    list_filter   = ('status','publish','category')
    search_fields = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Quiz,QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display  = ('title', 'quiz_to_str', 'answer_true', 'status')
    list_filter   = ('quiz', 'status')
    search_fields = ('title', 'title', 'answer_one', 'answer_two', 'answer_three', 'answer_four')


admin.site.register(Question,QuestionAdmin)
