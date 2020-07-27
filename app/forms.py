from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Catagory, SubCatagory, Products

# Apply summernote to specific fields.
class CatagoryForm(forms.ModelForm):
    # desc = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
    class Meta:
        model = Catagory
        widgets = {
            'cat_desc': SummernoteWidget()
            }
        fields = "__all__" 

class SubCatagoryForm(forms.ModelForm):
    class Meta: 
        model = SubCatagory
        widgets = {
            'cat_desc': SummernoteWidget()
            }
        fields = "__all__" 

class ProductsForm(forms.ModelForm):
    # catagory = forms.ModelMultipleChoiceField(queryset=SubCatagory.objects.all())
    class Meta:
        model = Products
        widgets = {
            'prod_desc': SummernoteWidget()
            }
        fields = "__all__" 
