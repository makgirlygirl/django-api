#from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Question,Paragraph
from .serializers import ParagraphSerializer,QuestionSerializer
from django.http import Http404
from rest_framework import status
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def get_paragraph_list(request):
    if request.method == 'GET':
        paragraphList = Paragraph.objects.all()
        serializer = ParagraphSerializer(paragraphList, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def post_paragraph(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ParagraphSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def get_a_paragraph(request, pk):
    object = Paragraph.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ParagraphSerializer(object)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def get_question_list(request):
    if request.method == 'GET':
        questionList = Question.objects.all()
        serializer = QuestionSerializer(questionList, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def post_question(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def get_a_question(request, pk):
    object = Question.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = QuestionSerializer(object)
        return JsonResponse(serializer.data, safe=False)
