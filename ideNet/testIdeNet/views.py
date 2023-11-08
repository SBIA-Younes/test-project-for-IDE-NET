from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import BlogPost


class AccountLoginView(LoginView):
    template_name = 'login.html'


def home(request):
    if not request.user.is_authenticated:
        blog_post = BlogPost.objects.filter(published=True, internet=True).order_by('-created_on')[:6]
    else:
        blog_post = BlogPost.objects.filter(published=True).order_by('-created_on')[:6]

    context = {
      "posts" : blog_post
    }
    return render(request, "base.html", context)
