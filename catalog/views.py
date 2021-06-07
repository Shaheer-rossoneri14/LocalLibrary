from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

from catalog import models
# Create your views here.

def index(request):
    #View Fn for home page.
    #Generate count of main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available books 
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#Generic class based views
class BookListView(generic.ListView):
    model = Book
    paginate_by=10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorLiistView(generic.ListView):
    model = Author
    paginate_by=10

class AuthorDetailView(generic.DetailView):
    model = Author