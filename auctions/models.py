from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass

class Category(models.Model):
    category_types = models.CharField(max_length=30)

class Listing(models.Model):
    #user that posted the listing
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="this_user_listings")
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True)
    startingbid = models.FloatField()
    currentbid = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="this_category_listings")
    imageurl = models.URLField(blank=True)
    isitactive = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="this_user_fav_listing")


class Bid(models.Model):
    #user that bid on this listing
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="this_user_bids")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="this_listing_bids")
    bidamount = models.FloatField()

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="this_user_comments")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="this_listing_comments")
    comment = models.CharField(max_length=255)

