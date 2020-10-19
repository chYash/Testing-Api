from rest_framework import serializers
from .models import * 
from datetime import datetime

class BugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bug
        fields = "__all__"

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"

# class MonthlyExpenseSerializer(serializers.ModelSerializer):

#     info = serializers.SerializerMethodField()

#     class Meta:
#         model = Expense
#         fields = []
    
#     def get_info(self,obj):
