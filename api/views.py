from email.policy import HTTP
from urllib import response
from django.shortcuts import render,get_object_or_404
from rest_framework import serializers,status

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from .serializers import BookSerializer,TagSerializer,TagBookLinkSerializer

# Imported models

from .models import Book,Tag,TagBookLink
from django.contrib.auth.models import User



# Create your views here.

@api_view(['POST','GET'])
@permission_classes([AllowAny])
def createUser(request):
    if request.method=='POST':
        try:
            user=User.objects.create_user(username=request.data['username'],email= request.data['email'],password= request.data['password'])
            user.save()
            token=Token.objects.create(user=user)
            token.save()
            return Response(data={'Info': ' User successfully created!'},status=status.HTTP_201_CREATED)
        except Exception:
            return Response(data={'Error': ' User creation ended in failure...'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={'Info':'This is where you create user'},status=status.HTTP_400_BAD_REQUEST)


            


@api_view(['POST','DELETE','GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AddOrRemoveBook(request):
    if request.method=='GET':
        return Response(data={'Error': ' Only \'POST\' and \'DELETE\' are allowed '},status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='POST':
        userID=request.user.id
        book=Book.objects.create(name=request.data['name'],
                                authors=request.data['authors'],
                                description=request.data['description'],
                                uploader=request.user,
                                file=request.data['file'])
        enteredTags=request.data['tags']
        allTags= Tag.objects.all()
        taglist= enteredTags.split(',')
        
        print(allTags)
        print("LOOP: Checking for existing tags and adding new ones")
        if enteredTags!='':
            for i in taglist:
                potentialtag= i.lower()
                if potentialtag not in allTags.values():
                    tag=Tag.objects.create(name=potentialtag)
                    tag.save()
                    tagbooklink=TagBookLink.objects.create(book=book,tag=tag)
                    tagbooklink.save()
                else:
                    tag=get_object_or_404(Tag,name=potentialtag)
                    tagbooklink=TagBookLink.objects.create(book=book,tag=tag)
                    tagbooklink.save()
            
        book.save()
        
        return Response(data={'Success':'Book Successfully Added'},status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        bookID=request.data['bookId']
        book=get_object_or_404(Book,id=bookID)
        if (book.uploader.id==request.user.id):
            book.delete()
            return Response(data={'Success': 'The book is deleted'},status=status.HTTP_200_OK)
        else:
            return Response(data={'Error': 'You are not permitted to delete a book you did not create!!!'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getMyProfileInfo(request,option):
    if request.method=='GET':
        if option=='partial':    
            context={'id':request.user.id,
                    'username':request.user.username,
                    'encryptedPassword':request.user.password,
                    'email':request.user.email
                    }
            return Response(data=context,status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getMyBooks(request):
    if request.method=='GET':
        mybooks=Book.objects.filter(uploader=request.user.id)
        serializer=BookSerializer(mybooks,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def viewBook(request,pk):
    if request.method=='GET':
        book=get_object_or_404(Book,id=pk)
        serializer=BookSerializer(book)
        tagLinks=TagBookLink.objects.filter(book=book.id)
        tags=[]
        for item in tagLinks:
            tags.append({'id':item.tag.id,'name':item.tag.name})
        

        return Response(data={'data':serializer.data,'tags':tags},status=status.HTTP_200_OK)



        
        


                                







