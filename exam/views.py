from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Question, Quiz, Category

# Create your views here.

class QuizListView(ListView):
    queryset = Quiz.objects.published()



def question_list(request,slug):
    quiz = get_object_or_404(Quiz, slug=slug, status=True)
    questions = quiz.question.published()
    context ={
        'quiz' : quiz,
        'questions' : questions,
    }
    return render(request, 'exam/question_list.html', context)

def quiz_result(request,slug):
    quiz = get_object_or_404(Quiz, slug=slug, status=True)
    if request.method == 'POST':
        number_true_answer = 0
        for question in request.POST:
            if question == 'csrfmiddlewaretoken':
                continue
            if int(request.POST[question]) == int(Question.objects.get(pk=int(question)).answer_true):
                number_true_answer += 1
        context = {
            'number_true_answer': number_true_answer,
            'quiz' : quiz
        }
        return render(request, 'exam/quiz_result.html', context)
