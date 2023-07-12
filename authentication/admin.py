from django.contrib import admin
from .models import User, Client, Admin, Loan, TransactionReport, Payment

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Loan)
admin.site.register(TransactionReport)
admin.site.register(Payment)


