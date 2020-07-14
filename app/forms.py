from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Apply summernote to specific fields.
class CatagoryForm(forms.Form):
    desc = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
