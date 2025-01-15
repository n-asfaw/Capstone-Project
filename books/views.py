from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'], url_path='available')
    def available_books(self, request):
        books = self.queryset.filter(copies_available__gt=0)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})