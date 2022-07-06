from django.contrib import admin
from .models import Account, Message,Friend,Group,Good

admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Good)
admin.site.register(Account)