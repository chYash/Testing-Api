from django.urls import path,include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()

app_name = 'dummyapis'

urlpatterns = [
	path("monthlyexpense/<int:id>", MonthlyExpenseViewSetAPI.as_view()),

]

router.register('bug', BugViewsetAPI, basename='Bug')
router.register('expense',ExpenseViewsetAPI,basename='Expense')
router.register('user',UserViewSetAPI,basename='User')

# router.register('monthlyexpense',MonthlyExpenseViewSetAPI,basename='Monthly-expense')

urlpatterns += router.urls