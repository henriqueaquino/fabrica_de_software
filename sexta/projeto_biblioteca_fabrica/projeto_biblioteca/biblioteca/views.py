from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Livro
from .serializers import LivroSerializer

@csrf_exempt
def livro_list(request):
    if request.method == 'GET':
        pessoas = Livro.objects.all()
        serializer = LivroSerializer(pessoas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LivroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def livro_detail(request, pk):
    try:
        pessoa = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LivroSerializer(pessoa)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LivroSerializer(pessoa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        pessoa.delete()
        return HttpResponse(status=204)