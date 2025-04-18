from django.urls import path
from .views import receive_ctg_list, grain_ctg

urlpatterns = [
    path('', receive_ctg_list, name='receive_ctg_list'),
    path('<int:pk>/', grain_ctg, name='grain_ctg'),
]