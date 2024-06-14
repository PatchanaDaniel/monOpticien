from django.contrib import admin
from monOpticien.models import Client
# Register your models here.
class ClientAdmin(admin.ModelAdmin):

    list_display = ('nom', 'motifs','date')
admin.site.register(Client,ClientAdmin)
