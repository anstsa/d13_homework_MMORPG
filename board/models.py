from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Advertisement(models.Model): 
    CATEGORY = [
        ('TK','Танки'),
        ('XL','Хилы'),
        ('DD','ДД'),
        ('TG','Торговцы'),
        ('GM','Гилдмастеры'),
        ('KG','Квестгиверы'),
        ('KU','Кузнецы'),
        ('KG','Кожевники'),
        ('ZE','Зельевары'),
        ('MZ','Мастера заклинаний')
    ]
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length = 150, default = '')
    text = models.TextField(default = '')
    datatime = models.DateTimeField(auto_now_add = True) 
    data = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='img', null=True, blank=True)
    video = models.FileField(upload_to='video', null=True, blank=True)
    files = models.FileField(upload_to='files', null=True, blank=True)
    category = models.CharField(choices=CATEGORY, max_length=2, default = 'TK')

    def __str__(self):
        return f'{self.title}'

    
    def get_absolute_url(self):   
        return f'/board/{self.id}'


class Response (models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField(default = '')
    datatime = models.DateTimeField(auto_now_add = True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    
     
