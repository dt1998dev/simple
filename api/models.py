
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self) :
        return f' #{self.id} {self.name}'


class Book(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    authors=models.CharField(max_length=250,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    uploadDate=models.DateField(auto_now_add=True,null=True)
    uploader=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(upload_to='books')

    def __str__(self):
        return f' #{self.id} {self.name} from {self.authors}'


class TagBookLink(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)

    def __str__(self) :
        return f' #{self.id} {self.book.name} Tag: {self.tag.name}'



    
