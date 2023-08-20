from django_filters import FilterSet # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Response, Advertisement 
from django_filters import filters 

 
 
# создаём фильтр
class ResponseFilter(FilterSet):
    advertisement = filters.ModelChoiceFilter (label = "Выбрать обьявления",
            queryset = Advertisement.objects.all())


    class Meta:
        model = Response
        fields = ('advertisement',) 