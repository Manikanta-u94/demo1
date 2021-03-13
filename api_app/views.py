from django.shortcuts import render
from .models import post
from .serializers import postserializer
from django.http import Http404

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class PostViews(APIView):


	def get(self, request, format=None):
	    qs = post.objects.all()
	    serializer = postserializer(qs, many=True)
	    return Response(serializer.data)

	def post(self, request, format=None):
	    serializer = postserializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data, status=status.HTTP_201_CREATED)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class postDetail(APIView):

	parser_class = (FileUploadParser,)

	# def get_object(self, pk):

	# 	qs = post.objects.get(pk=pk)
	# 	serializer = postserializer(qs)
	# 	return Response(serializer.data)


	def get(self, request, pk, format=None):
	    post = self.get_object(pk)
	    serializer = postserializer(post)
	    return Response(serializer.data)

	def put(self, request, pk, format=None):
	    post = self.get_object(pk)
	    serializer = postserializer(post, data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
	    post = self.get_object(pk)
	    post.delete()
	    return Response(status=status.HTTP_204_NO_CONTENT)













