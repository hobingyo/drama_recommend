from django.shortcuts import render, redirect
from .models import ArticleModel
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/article')
    else:
        return redirect('/sign-in')


def article(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_tweet = ArticleModel.objects.all().order_by('-created_at')
            return render(request, 'article/upload.html', {'tweet': all_tweet})
        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        user = request.user
        title = request.POST.get('title', '')
        synopsis = request.POST.get('synopsis', '')
        genre = request.POST.get('genre', '')
        cast = request.POST.get('cast', '')
        aired_date = request.POST.get('aired_date', '')
        episode = request.POST.get('episode', '')
        aged = request.POST.get('aged', '')

        my_article = ArticleModel.objects.create(author=user, title=title, synopsis=synopsis, genre=genre,
                                                 cast=cast, aired_date=aired_date, episode=episode, aged=aged, rating = 0)
        my_article.save()
        return redirect('/tweet')
