from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from rest_framework import serializers
from django import forms

from .models import (
    Catagory, 
    SubCatagory, 
    Products,
    RelProducts,
    ProductsReview
)


# Product serializer add related-products 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__' 

""" Catagory """
class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        # summernote widget
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


""" Products """
class ProductBasicInfoForm(forms.ModelForm):
    class Meta:
        model = Products
        widgets = {
            'prod_desc': SummernoteWidget()
            }
        fields = [
            'prod_name',
            'sku',
            'catagory',
            'prod_img',
            'allow_to_attach_file',
            'is_avail_to_sell',
            'prod_desc',
        ] 


class ProductPriceInventoryForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'price',
            'sell_price',
            'arrival_date',
            'is_inventory_track',
            'quantity_in_stock',
        ] 


class ProductShippingForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'weight',
            'req_shipping',
            'shipping_price',
        ] 

class RelProductsForm(forms.ModelForm):
    class Meta:
        model = RelProducts
        fields = '__all__'

""" Product Review """
class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductsReview
        fields = '__all__'
