from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView
from .models import Advertisement, User
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ResponseFilter
from django.shortcuts import redirect

 
class AdvertisementList(ListView):
    model = Advertisement  
    template_name = 'advertisements.html'  
    context_object_name = 'advertisements'
    queryset = Advertisement.objects.order_by('-id')
    paginate_by = 6

class AdvertisementDetail(DetailView):
    model = Advertisement 
    template_name = 'advertisement.html' 
    context_object_name = 'advertisement'
    queryset = Advertisement.objects.all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        id_author = list(Advertisement.objects.filter(pk=self.kwargs['pk']).values("author")[0].values())[0]
        author = User.objects.get(id=id_author)
       
        context = super().get_context_data(**kwargs)
        if user == author:
            context['user_authors'] = user.username

        context['form'] = ResponseForm()
        context['responses'] = Response.objects.filter(advertisement=self.object.pk, accepted = True).select_related('author')
       
        return context


class SetAuthorMixin(LoginRequiredMixin):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdvertisementAddView(SetAuthorMixin, CreateView):
   template_name = 'advertisement_add.html'
   form_class = AddAdvertisementForm

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddAdvertisementForm()
        return context

class AdvertisementEditView(SetAuthorMixin, UpdateView):
   template_name = 'advertisement_add.html'
   form_class = AddAdvertisementForm

   def get_object(self, **kwargs):
       id = self.kwargs.get('pk')
       return Advertisement.objects.get(pk=id)

class AdvertisementDeleteView(SetAuthorMixin, DeleteView):
   template_name = 'advertisement_delete.html'
   queryset = Advertisement.objects.all()
   context_object_name = 'advertisement'
   success_url = '/board/'

class ResponseAddView(SetAuthorMixin, CreateView):
    template_name = 'advertisement.html' 
    form_class = ResponseForm
    success_url = '/board/responses/checked_out'
    
    def form_valid(self, form):
        form.instance.advertisement_id = self.kwargs['pk']
        return super().form_valid(form)

class ResponseView(LoginRequiredMixin, ListView):
    """Показывает все отклики к моим объявлениям"""
    model = Response
    template_name = 'user_response.html'

    def get_queryset(self):
        return Response.objects.filter(advertisement__author=self.request.user).select_related('author', 'advertisement').order_by('-datatime')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset()) 
        return context

def response_delete(request, pk):
    """Удалить отклик"""
    response = Response.objects.get(id=pk)
    if response:
        response.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def response_accept(request, pk):
    """Принять отклик"""
    response = Response.objects.get(id=pk)
    if response:
        response.accepted = True
        response.save()
    return redirect(request.META.get('HTTP_REFERER'))

class ResponseCheckedView(ListView):
    template_name = 'checked_out.html'
    model = Response
    context_object_name = 'response'
    queryset = Response.objects.order_by('-id')


    
