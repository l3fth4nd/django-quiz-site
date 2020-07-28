from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Question, Quiz, Category

# Create your views here.

def quiz_list(request):
    return HttpResponse('hello')

def question_list(request,slug):
    quiz = get_object_or_404(Quiz, slug=slug, status=True)
    questions = quiz.question.published()
    context ={
        'quiz' : quiz,
        'questions' : questions,
    }
    return render(request, 'exam/question_list.html', context)
