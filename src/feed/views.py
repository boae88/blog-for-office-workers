from django.shortcuts import render
from .models import Article, Comment, HashTag

# Create your views here.
def index(request):
    article_list= Article.objects.all()
    hashtag_list= HashTag.objects.all()

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list
    }
    return render(request, "index.html", ctx)



def detail(request):
    pass

# def about(request):
    # pass
