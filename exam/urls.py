from django.urls import path
from .views import quiz_list, question_list


app_name = 'quiz'
urlpatterns = [
    path('',quiz_list,name='quiz_list'),
    path('quiz/<slug:slug>', question_list, name='question_list'),
]
