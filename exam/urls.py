from django.urls import path
from .views import quiz_list, question_list, quiz_result


app_name = 'exam'
urlpatterns = [
    path('',quiz_list,name='quiz_list'),
    path('quiz/<slug:slug>', question_list, name='question_list'),
    path('quiz/<slug:slug>/result', quiz_result, name='quiz_result'),
]
