from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Transaction
from books.models import Book
from .serializers import TransactionSerializer
from django.utils.timezone import now 
from django.shortcuts import render

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['post'], url_path='checkout')
    def checkout_book(self, request):
        user = request.user
        book_id = request.data.get('book_id')
        book = Book.objects.get(id=book_id)

        if book.copies_available <= 0:
            return Response({"error": "No copies available."}, status=status.HTTP_400_BAD_REQUEST)

        Transaction.objects.create(user=user, book=book)
        book.copies_available -= 1
        book.save()
        return Response({"message": "Book checked out successfully."})

    @action(detail=False, methods=['post'], url_path='return')
    def return_book(self, request):
        user = request.user
        transaction_id = request.data.get('transaction_id')
        transaction = Transaction.objects.get(id=transaction_id, user=user)

        if transaction.return_date:
            return Response({"error": "Book already returned."}, status=status.HTTP_400_BAD_REQUEST)

        transaction.return_date = now().date()
        transaction.save()
        book = transaction.book
        book.copies_available += 1
        book.save()
        return Response({"message": "Book returned successfully."})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})


def transaction_detail(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_detail.html', {'transactions': transactions})