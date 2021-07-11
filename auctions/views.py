from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ListingForm, BidForm
from .models import User, Listing, Category, Bid, Comment
from django.contrib import messages


def index(request):
    return render(request, "auctions/index.html", {
        "activelistings":Listing.objects.filter(isitactive= True)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def createlisting(request):
    form = ListingForm()
    if request.method == "POST":
        #must add request.FILES since image file is coming too
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user_id = request.user
            listing.save()
    return render(request, "auctions/createlisting.html", {
        "form":form
    })


def addtowatch(request, listing_id):

    listing = Listing.objects.get(pk=listing_id) 

    if request.method == 'POST':
        if listing not in request.user.this_user_fav_listing.all():
            request.user.this_user_fav_listing.add(listing)
            
        else:
            request.user.this_user_fav_listing.remove(listing)

    return HttpResponseRedirect(reverse('listing', kwargs={"listing_id":listing_id}))


def listing(request, listing_id):
    
    listing = Listing.objects.get(pk=listing_id)
    form = BidForm()

    if listing in request.user.this_user_fav_listing.all():
        value = 'Remove from'
    else:
        value = 'Add to'   

    return render(request, "auctions/listing.html", {
        "listing":listing,
        "form": form,
        "value": value
    })

def bid(request, listing_id):
    listing = Listing.objects.get(pk = listing_id)
    if listing.currentbid == None:
        bid = listing.startingbid
        print(bid)
    else:
        bid = listing.currentbid
    if request.method == "POST":

        form = BidForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['bidamount'] <= bid:
                messages.error(request, 'This amount is lower or equal to the current bid. Please add a higher amount to bid on this listing.')
            else:
                bidrow = form.save(commit=False)
                bidrow.user_id = request.user
                bidrow.listing_id = listing
                bidrow.save()
                listing.currentbid = form.cleaned_data['bidamount']
                listing.save()
                messages.success(request, 'Bid successfully placed, your bid is now the highest current bid.')

    return HttpResponseRedirect(reverse('listing', kwargs={"listing_id":listing_id}))