from django.contrib import admin
from django.urls import path
from book_api.views import BookList,BookCreate,BookDetail
#book_list,book_create,book

urlpatterns = [
    #path('', book_create),
    #path('list/', book_list),
    #path('<int:pk>', book)
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>', BookDetail.as_view()),
]