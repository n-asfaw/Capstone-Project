from rest_framework import serializers
from .models import Book
import re

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'copies_available']

def validate_isbn(value):
    if not re.match(r'^\d{13}$', value):
        raise serializers.ValidationError("ISBN must be a 13-digit number.")
    return value
