from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class User(AbstractUser):
    pass

class Category(models.Model):
    category_types = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category_types}"

class Listing(models.Model):
    #user that posted the listing
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="this_user_listings")
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    startingbid = models.FloatField()
    currentbid = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="this_category_listings", blank=True, null=True)
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    isitactive = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="this_user_fav_listing")
    dateposted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}: {self.description}"

    def get_starting_bid(self):
        return "{:.2f}".format(self.startingbid)

    def get_current_price(self):
        if self.currentbid is None:
            return "$" + "{:.2f}".format(self.startingbid)
        else:
            return "$" + "{:.2f}".format(self.currentbid)

    def get_date(self):
        return self.dateposted.strftime("%b. %d, %Y, %I:%M %p")

class Bid(models.Model):
    #user that bid on this listing
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="this_user_bids")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="this_listing_bids")
    bidamount = models.FloatField()
    datebidded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidamount}"

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="this_user_comments")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="this_listing_comments")
    comment = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id.username}: {self.comment} @ {self.time}"

    def get_date(self):
        return self.time.strftime("%b. %d, %Y, %I:%M %p")




