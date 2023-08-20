from django.forms import ModelForm
from .models import Advertisement, Response
from django import forms

class AddAdvertisementForm(ModelForm):
  class Meta:
      model = Advertisement
      fields = ['title', 'text',
                'image', 'video',
                'files', 'category',
              ]
      labels = {
            'title': ('Заголовок'),
            'text': ('Текст объявления'),
            'image': ('Изображение'),
            'video': ('Видео'),
            'files': ('Файлы'),
            'category': ('Категория'),
      }
      widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
        'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст объявления'}),
        'category': forms.RadioSelect(attrs={'name': 'rating'}),
     }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']
        labels = {
            'text': ('Добавить отклик:'),
        }
        widgets = {
           'text': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите текст отклика'
       }),
     }
