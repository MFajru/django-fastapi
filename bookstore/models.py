from django.db import models

class BaseModel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class Book(BaseModel):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    published_date = models.DateField()

    def __str__(self):
        return self.title
