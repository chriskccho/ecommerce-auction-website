from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("listing/addtowatch/<int:listing_id>", views.addtowatch, name="addtowatch"),
    path("listing/bid/<int:listing_id>", views.bid, name="bid"),
    path("listing/comment/<int:listing_id>", views.comment, name="comment"),
    path("listing/close/<int:listing_id>",views.close,name="close"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categorylisting/<int:category_id>", views.categorylisting, name="categorylisting"),
    path("nocategory", views.nocategory, name="nocategory"),
    path("mylisting", views.mylisting, name="mylisting"),
    path("mybid", views.mybid, name="mybid")
]

