from django.urls import path
from .views import AdvertisementList, AdvertisementDetail, AdvertisementAddView
from .views import AdvertisementEditView, AdvertisementDeleteView
from .views import ResponseAddView, ResponseView, response_accept, response_delete, ResponseCheckedView
 
urlpatterns = [
    path('', AdvertisementList.as_view(), name='list_ad'),
    path('<int:pk>', AdvertisementDetail.as_view(), name='advertisement'),
    path('add/', AdvertisementAddView.as_view(), name = 'add_advertisement'),
    path('<int:pk>/edit/', AdvertisementEditView.as_view(), name='edit_advertisement'),
    path('<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='delete_advertisement'),
    path('<int:pk>/response/', ResponseAddView.as_view(), name='add_response'),
    path('responses/', ResponseView.as_view(), name='all_responses'),
    path('responses/<int:pk>/accept', response_accept, name='response_accept'),
    path('responses/<int:pk>/delete', response_delete, name='response_delete'),
    path('responses/checked_out', ResponseCheckedView.as_view(), name='checked_out')
    

]


