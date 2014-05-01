from models import *
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class ReadBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadBook


class CodingPrinciplesBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingPrinciplesBook


class PersonalDevelopmentBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDevelopmentBook


class ReadingListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListBook