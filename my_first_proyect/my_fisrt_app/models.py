
from django.db import models

# Create your models here.


class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True) #Este campo puede quedar vacio con null=true
    color = models.TextField(max_length=25, null=True)
    def __str__(self):
        return f"{self.title} - {self.year}"
    
class Publisher(models.Model):
    name = models.TextField(max_length=200)
    
    address = models.TextField(max_length=200)
    
    def __str__(self):
        return f"{self.name} - {self.address}"

class Author(models.Model):
    name = models.TextField(max_length=100)
    birth_date = models.DateField()
    

    def __str__(self):
        return f"{self.name} "
    
class Profle(models.Model):
    author = models.OneToOneField(Author,on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.author} - {self.website} - {self.biography}"


class Book(models.Model):
    title = models.TextField(max_length=200)
    
    publication_date = models.DateField()
    
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)

    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return f"{self.title} - {self.publisher} - {self.authors}"

