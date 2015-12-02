from django import forms
from .models import *
class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Photos', 'Category', 'Title', 'Description','BidStart','Till','Timer']

class BidPostForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['BidPrice']

class SearchProductForm(forms.Form):
    name = forms.CharField();

class CategorySearchForm(forms.ModelForm):
   class Meta:
      model = Product
      fields = ['Category']

