from .views import get_list_ctg, detail_ctg, CategoryViewSet
from django.urls import path

urlpatterns = [
    path('', get_list_ctg, name='list'),
    path('<int:pk>/', detail_ctg , name='id'),
    path('ctl/', CategoryViewSet.as_view(), name='ctl' )
]