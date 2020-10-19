from rest_framework import serializers
from .models import * 
import datetime 

class BugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bug
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"

class MonthlyExpenseSerializer(serializers.ModelSerializer):

    lastMonth = serializers.SerializerMethodField(read_only =True)
    currentMonth = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["lastMonth","currentMonth"]
    
    def get_lastMonth(self,obj):
        today = datetime.date.today()
        money = Expense.objects.filter(user=obj.id,date__month = (today.month-1))
        totalExpense=0
        totalIncome =0
        for i in money:
            totalExpense = totalExpense + i.expense
            totalIncome = totalIncome + i.income
        
        data ={
            "totalExpense":totalExpense,
            "totalIncome":totalIncome
        }
        return data

    def get_currentMonth(self,obj):
        today = datetime.date.today()
        money = Expense.objects.filter(user=obj.id,date__month = today.month)
        totalExpense=0
        totalIncome =0
        for i in money:
            totalExpense = totalExpense + i.expense
            totalIncome = totalIncome + i.income
        
        data ={
            "totalExpense":totalExpense,
            "totalIncome":totalIncome
        }
        return data