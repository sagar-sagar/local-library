
from django.shortcuts import render

# Create your views here.
from .models import *

'''
Books
Copies
Copies available
Authors

'''

def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_genre': num_genre
    }
    
    return render(request,'index.html',context=context)

from django.views import generic
class BookListView(generic.ListView):
    model = Book
    
class BookDetailView(generic.DetailView):
    model = Book