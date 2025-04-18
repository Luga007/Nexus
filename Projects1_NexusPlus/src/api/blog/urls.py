from django.urls import path
from .views import obtain_list_tg, fraction_ctg
urlpatterns = [
    path('', obtain_list_tg, name='obtain_list_tg'),
    path('<int:pk>/', fraction_ctg, name='fraction_ctg'),
]