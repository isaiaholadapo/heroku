from django.contrib import admin

from transaction.models import Deposit, AccountDetail, Withdraw, Transfer, History
# Register your models here.

class DepositAdmin(admin.ModelAdmin):
    list_display = [ 'amount', 'dep_email', 'dep_account', 'date',]

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['email', 'withdraw_account', 'withdraw_amount', 'date',]

class TransferAdmin(admin.ModelAdmin):
    list_display = ['email', 'receiver_account', 'amount', 'date',]

class InterestAdmin(admin.ModelAdmin):
    list_display = ['email', 'interest', 'date',]

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['email', 'receiver_account', 'amount', 'date',]

admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(AccountDetail)
admin.site.register(History)
