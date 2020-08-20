from django.test import TestCase
from .forms import ProductReviewForm
from .models import ProductsReview

class ProductReviewTest(TestCase):
    def setUp(self):
            ProductsReview.objects.create(rating="lion", reviewer_name="roar")
            ProductsReview.objects.create(rating="cat", reviewer_name="meow")
