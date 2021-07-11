from django.forms import ModelForm
from .models import Listing, User, Category, Bid, Comment

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        labels = {
            "startingbid": "Starting bid",
        }
        fields = ['title', 'description', 'startingbid', 'category', 'image']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        labels = {
            "bidamount": "Offer"
        }
        fields = ['bidamount']

        