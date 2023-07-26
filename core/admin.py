from django.contrib import admin
from .models import User, Client, Admin, Loan, Payment

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Loan)
admin.site.register(Payment)


