from django.db import models 

class Book(models.Model):
    book_title = models.CharField('Название книги', max_length = 300)
    date_issue = models.DateTimeField('Дата выдачи книги',blank=True,null=True)
    date_return = models.DateTimeField('Дата возврата книги',blank=True,null=True)

    def __str__(self):
        return self.book_title
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Author(models.Model):
    book = models.ManyToManyField(Book)
    author_name = models.CharField('Имя автора', max_length = 200)
    email = models.EmailField(blank=True)
    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
