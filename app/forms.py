from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Catagory, SubCatagory

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