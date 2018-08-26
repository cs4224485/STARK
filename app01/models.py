from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(verbose_name="书籍名称", max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ManyToManyField('Author', )
    publish = models.ForeignKey('Publish', on_delete=True, default='1')

    def __str__(self):
        return self.title

class Publish(models.Model):
    title = models.CharField(verbose_name="出版社名称", max_length=32)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=24)
    age = models.IntegerField()
    email = models.EmailField(default='414804000@qq.com')
    def __str__(self):
        return self.name

