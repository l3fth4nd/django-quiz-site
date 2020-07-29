from django.urls import path
from .views import question_list, quiz_result, QuizListView


app_name = 'exam'
urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
    path('quiz/<slug:slug>', question_list, name='question_list'),
    path('quiz/<slug:slug>/result', quiz_result, name='quiz_result'),
]
