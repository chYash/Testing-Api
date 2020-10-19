from django.contrib import admin


from .models import *

admin.site.register(Bug)
admin.site.register(User)
admin.site.register(Expense)