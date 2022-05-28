from django.urls import path, include
from .views import get_paragraph_list, get_question_list, get_a_paragraph, get_a_question, post_paragraph, post_question

urlpatterns = [
    path("paragraph", get_paragraph_list),
    path('paragraph/<int:pk>', get_a_paragraph),
    path("new_paragraph", post_paragraph),
    path("question", get_question_list),
    path('question/<int:pk>', get_a_question),
    path("new_question", post_question),
]