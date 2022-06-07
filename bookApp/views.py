from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books
from .serializers import BooksSerializer
from rest_framework import status
from rest_framework import serializers
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({
        'message': 'Achieved',
        'code': 200
    })


@api_view(['GET'])
def get_all_books(request):
    # b = list(Books.objects.all().values())
    # return JsonResponse(b, safe=False)
    b = Books.objects.all()
    serializer = BooksSerializer(b, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def getBook(request, pk):
    book = Books.objects.get(id=pk)
    serializer = BooksSerializer(book)
    return Response(serializer.data)



@api_view(['POST'])
def createBook(request):
    book_item = BooksSerializer(data=request.data)
    # validating for already existing data
    if Books.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    try:
        if book_item.is_valid():
            book_item.save()
            return Response(book_item.data)
    except Exception as e:    
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_books(request, id):
    item = Books.objects.get(pk=id)
    data = BooksSerializer(item, data=request.data, partial=True)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



