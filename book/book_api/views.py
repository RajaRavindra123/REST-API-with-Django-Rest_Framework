'''from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from book_api.models import Book
from book_api.serailizer import BookSerializer
# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all() # Complex Data
    serailizer = BookSerializer(books, many=True)
    return Response(serailizer.data) 
#End point /book/list/

@api_view(['POST'])
def book_create(request):
    serailizer = BookSerializer(data=request.data)
    if serailizer.is_valid():
        serailizer.save()
        return Response(serailizer.data)
    else: 
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except:
        return Response({
            'error': 'Book Does NOT Exist '
        }, status=status.HTTP_404_NOT_FOUND)
        
        
    if request.method == 'GET':
        serailizer = BookSerializer(book)
        return Response(serailizer.data)
    
    if request.method == 'PUT':
        serailizer = BookSerializer(book, data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
    
    
        
from rest_framework.views import APIView
from book_api.models import Book
from book_api.serailizer import BookSerializer
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self, request):
         books = Book.objects.all() # Complex Data
         serailizer = BookSerializer(books, many=True)
         return Response(serailizer.data) 
     
    
class BookCreate(APIView):
    def post(self,request):
        serailizer = BookSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        else: 
            return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
class BookDetail(APIView):
    def get_book_by_pk(self,  pk):  
        try:
           return Book.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Book Does NOT Exist '
            }, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serailizer = BookSerializer(book)
        return Response(serailizer.data)
        
    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serailizer = BookSerializer(book, data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     
     