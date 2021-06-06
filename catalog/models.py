from django.db import models
from django.db.models.fields import UUIDField
from django.urls import reverse     #Generate URLs by reversing the URL patterns 
import uuid     #for unique book instances
# Create your models here.
#Model representing Book genre
class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre (e.g. Fiction/Mystery etc)')

    def __str__(self):
        return self.name

#Model representing a book ("NOT SPECIFIC COPY")
class Book(models.Model):
    title = models.CharField(max_length=200)
    #author as Foriegn key as book can have one author only in this implementation
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #Returns the url to access a detail record for this book.
        return reverse('book-detail', args=[str(self.id)])

#Model representing a SPECIFIC COPY OF BOOK
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT,null=True)
    due_back = models.DateField(null=True, blank=True)

    #Tuple passed to choices
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availabilty'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

#Model representing an author
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    