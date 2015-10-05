from appy.models import Question
from rest_framework import serializers


class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (['question_text'])
