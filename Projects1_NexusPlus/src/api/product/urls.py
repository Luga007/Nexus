from django.urls import path
from .views import aquire_ctg_list, fraction_ctg

urlpatterns = [
    path('', aquire_ctg_list, name='aquire_ctg_list'),
    path('<int:pk>/', fraction_ctg, name='fraction_ctg'),
]