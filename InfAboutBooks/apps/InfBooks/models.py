from django.db import models

class Book(models.Model):
    book_title = models.CharField('Название книги', max_length = 300)

    def __str__(self):
        return self.book_title
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"



class Author(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

 
#    def how_much_book(self):
        #return self.type_cat.count()
