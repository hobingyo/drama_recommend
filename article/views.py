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
            random_article = ArticleModel.objects.order_by("?").first()

            return render(request, 'article/home.html', {'article': all_article, 'random_article': random_article})
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
    article_comment = ArticleComment.objects.filter(article_id=id).order_by('-created_at')
    my_like = UserLike.objects.filter(user_id=request.user.id, article_id=id)
    return render(request, 'article/article_detail.html', {'article': my_article, 'comment': article_comment, 'like': my_like})

@login_required
def write_comment(request, id):
    if request.method == 'POST':
        current_article = ArticleModel.objects.get(id=id)
        user = request.user
        my_comment = ArticleComment()
        my_comment.author = user
        my_comment.comment = request.POST.get('comment', '')
        my_comment.rating = int(request.POST.get('rating', ''))
        my_comment.article = current_article
        my_comment.save()


        comment_rating = ArticleComment.objects.filter(article_id=id)
        rate = 0
        for rating in comment_rating:
            rate=rate+rating.rating
        current_article.rating=rate/len(comment_rating)
        current_article.save()

        return redirect('/article/'+str(id))

@login_required
def delete_comment(request, id):
    my_comment = ArticleComment.objects.get(id=id)
    my_comment.delete()

    current_article = ArticleModel.objects.get(id=my_comment.article_id)
    comment_rating = ArticleComment.objects.filter(article_id=my_comment.article_id)
    rate = 0
    for rating in comment_rating:
        rate = rate + rating.rating
    current_article.rating = rate / len(comment_rating)
    current_article.save()
    return redirect('/article/'+str(my_comment.article_id))

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

def search(request):
    search = request.POST.get('search','')
    my_search = ArticleModel.objects.all().filter(title__contains=search)
    return render(request, 'article/search.html', {'article': my_search})