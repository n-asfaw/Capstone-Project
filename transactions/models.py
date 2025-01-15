from django.db import models
from books.models import Book
from users.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} -> {self.book.title}"

@login_required
def user_borrowing_history(request):
    # Filter transactions for the logged-in user
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'borrowing_history.html', {'transactions': transactions})