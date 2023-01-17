from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add1/', views.add, name='add'),
    path('add1/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='updaterecord'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]