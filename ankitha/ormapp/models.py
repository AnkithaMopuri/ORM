from django.db import models
from django.contrib import admin
class Book(models.Model):
    title=models.CharField(max_length=20);
    year_of_publishing=models.DateField();
    Book_id=models.CharField(max_length=20,primary_key=True);
    author_name=models.CharField(max_length=15);
    number_of_pages=models.IntegerField();
    book_price=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
   list_display=("title","year_of_publishing","author_name","number_of_pages","book_price");