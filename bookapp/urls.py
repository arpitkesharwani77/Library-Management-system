from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListBook.as_view(), name='listbook'),
    path('detailbook/<int:pk>/', views.DetailBook.as_view(), name='detailbook'),
    path('create/', views.BookFormView.as_view(), name='createbook'),
    path('updatebook/<int:pk>/', views.UpdateBook.as_view(), name='updatebook'),
    path('deletebook/<int:pk>/', views.DeleteBook.as_view(), name='deletebook'),
    path('success/', views.SuccessView.as_view(), name='book_success'),
]
