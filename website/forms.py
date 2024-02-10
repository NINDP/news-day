from .models import Reviews
from django.forms import ModelForm


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ["text"]