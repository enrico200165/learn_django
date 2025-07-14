from django.contrib import admin
from .models import Item
# Register your models here.
admin.site.register(Item)
forms py
from django import forms
from .models import Item
 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_desc','item_price','item_image']
