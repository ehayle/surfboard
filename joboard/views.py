from django.shortcuts import render
from joboard.models import Post

def home(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "joboard/home.html", context)


def listing_details(request, listing_id):
    post = Post.objects.get(pk=listing_id)
    context = {
        "post": post,
        
    }

    return render(request, "joboard/listing_details.html", context)