from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *

from django.core import serializers

from rest_framework_jwt.utils import jwt_decode_handler
import jwt


from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from django.utils.decorators import method_decorator


from rest_framework import viewsets

class BugViewsetAPI(viewsets.ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

class ExpenseViewsetAPI(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class UserViewSetAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MonthlyExpenseViewSetAPI(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = MonthlyExpenseSerializer

    def retrieve(self,request,*args,**kwargs):

        user = self.queryset.get(user=kwargs["id"])
        serializer = self.serializer_class(user)
        return Response(serializer.data)