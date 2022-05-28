# models의 값을 json으로 변환해주는 역할
from rest_framework import serializers
from .models import Paragraph,Question

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('paragraphId', 'paragraphBody')
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('questionId', 'paragraph','questionTitle', 'answer','distractor1','distractor2','distractor3','distractor4')