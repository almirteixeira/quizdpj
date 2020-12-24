from django.contrib import admin
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import *

from .models import Question, Client, Product

class ClientAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'name', 'code')
    fields = ('user',  'cnpj', 'name', 'code', 'year', 'active')
    readonly_fields = ['code']
    search_fields = ['name']

    def get_queryset(self, request):
        query = super(ClientAdmin, self).get_queryset(request)
        filtered_query = query.filter(active=True, year=2019)
        return filtered_query

    
class ProductAdmin(admin.ModelAdmin):

    list_display = ('client_form', 'participation', 'segment', 'condition', 'layout',
                    'layoutuqbar', 'status')

    readonly_fields = ['layout', 'status']
    search_fields = ['client__name',
                     'client__cnpj', 'participation', 'segment']
    list_filter = ['participation', 'segment',
                   'condition', 'layout', 'layoutuqbar', 'status']

    def get_queryset(self, request):
        query = super(ProductAdmin, self).get_queryset(request)
        filtered_query = query.filter(client__active=True)
        return filtered_query

    
    def client_form(self, obj):
        return format_html(
            str(obj.client)
        )







# Register your models here.
admin.site.register(Question)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
