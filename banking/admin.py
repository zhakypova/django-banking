from django.contrib import admin

from .models import Client, Account, Credit, MyModel

admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Credit)
admin.site.register(MyModel)


