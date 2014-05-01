from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from models import *
from serializers import *

from json import dumps, loads, JSONEncoder


# Create your views here.
class NestedBookList(serializers.Serializer):
    read_books = ReadBookSerializer(many=True)

@api_view(('GET',))
def nested_book_list(request):
    read_books = ReadBook.objects.all()
    reading_list_books = ReadingListBook.objects.all()
    coding_principles_books = CodingPrinciplesBook.objects.all()

    serialized_read_books = ReadBookSerializer(read_books)
    serialized_reading_list_books = ReadingListBookSerializer(reading_list_books)
    serialized_coding_principles_books = CodingPrinciplesBookSerializer(coding_pricinples_books)

    result = {
        'read_books': serialized_read_books.data,
        'reading_list_books': serialized_reading_list_books.data,
        'coding_principles_books': serialized_coding_principles_books.data,
    }

    return Response(dumps(result), status=status.HTTP_201_CREATED)

