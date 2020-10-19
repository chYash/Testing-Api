from django.urls import path,include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()

# core routers

router.register('bug', BugViewsetAPI, basename='Bug')
router.register('expense',ExpenseViewsetAPI,basename='Expense')