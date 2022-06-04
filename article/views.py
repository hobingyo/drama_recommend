from django.shortcuts import render, redirect
from .models import ArticleModel, ArticleComment, UserLike
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
            all_article = ArticleModel.objects.all()
            return render(request, 'article/home.html', {'article': all_article})
        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        user = request.user
        title = request.POST.get('title', '')
        poster = request.POST.get('poster', '')
        synopsis = request.POST.get('synopsis', '')
        genre = request.POST.get('genre', '')
        cast = request.POST.get('cast', '')
        aired_date = request.POST.get('aired_date', '')
        episode = request.POST.get('episode', '')
        aged = request.POST.get('aged', '')

        my_article = ArticleModel.objects.create(author=user,poster=poster, title=title, synopsis=synopsis, genre=genre,
                                                 cast=cast, aired_date=aired_date, episode=episode, aged=aged, rating = 0)
        my_article.save()
        return redirect('/article')

@login_required
def detail_article(request, id):
    my_article = ArticleModel.objects.get(id=id)
    article_comment = ArticleComment.objects.filter(tweet_id=id).order_by('-created_at')
    my_like = UserLike.objects.filter(user_id=request.user.id, article_id=id)
    return render(request, 'article/article_detail.html', {'article': my_article, 'comment': article_comment, 'like': my_like})

@login_required
def write_comment(request, id):
    if request.method == 'POST':
        current_tweet = ArticleModel.objects.get(id=id)
        user = request.user

        my_comment = ArticleComment()
        my_comment.author = user
        my_comment.comment = request.POST.get('comment', '')
        my_comment.rating = int(request.POST.get('rating', ''))
        my_comment.tweet = current_tweet
        my_comment.save()
        return redirect('/article/'+str(id))

@login_required
def like(request, id):
    me = request.user
    article = ArticleModel.objects.get(id=id)
    my_like = UserLike.objects.filter(user_id=me.id, article_id=id)
    if my_like:
        my_like.delete()
    else:
        my_like = UserLike()
        my_like.article_id = article.id
        my_like.user_id = me.id
        my_like.save()

    return redirect('/article/'+str(id))

def like_listing(request):
    me = request.user
    likes = UserLike.objects.filter(user_id=me.id)
    article = []
    for like in likes:
        article += ArticleModel.objects.filter(id=like.article_id)
    return render(request, 'article/like.html', {'article': article})