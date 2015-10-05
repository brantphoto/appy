from django.shortcuts import render
from appy.models import Question
from rest_framework import viewsets
from appy.serializers import QuestionsSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-question_text')
    serializer_class = QuestionsSerializer


# Create your views here.
