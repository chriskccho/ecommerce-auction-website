from .models import Listing, Bid, Comment
from django import forms

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        labels = {
            "startingbid": "Starting bid",
        }
        fields = ['title', 'description', 'startingbid', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs= {'class':'form-control'}),
            'description': forms.Textarea(attrs = {'class':'form-control'}),
            'startingbid': forms.NumberInput(attrs = {'class': 'form-control'}),
            'category': forms.Select(attrs = {'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs = {'class': 'form-control-file'})
        }

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        labels = {
            "bidamount": "Offer"
        }
        fields = ['bidamount']
        widgets = {
            'bidamount': forms.NumberInput(attrs = {'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'class':'form-control'})
        }