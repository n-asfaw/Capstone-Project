"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from transactions.views import transaction_list
from transactions.views import transaction_detail
from books.views import book_list
from users.views import login


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # This includes login, logout, and password reset views
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/users/', include('users.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('books/', transaction_list, name='book_list'),
    path('transactions/', transaction_list, name='transactions_list'),
    path('transactions/', transaction_detail, name='transactions_detail'),
    path('books/', book_list, name='book_list'),
      # Login view, which uses the built-in login view
    path('users', login, name='login'),  # Or use Django's default login view if not custom
   

    # # Borrowing history page, protected by login_required
    # path('accounts/borrowing-history/', views.user_borrowing_history, name='user_borrowing_history'),
    
    # Optionally, you can add a logout link, which can be handled by Django's built-in logout view
    

    


]
