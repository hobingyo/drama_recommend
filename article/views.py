from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from .models import ArticleComment, UserLike, ArticleList, ArticleRecomm
from django.contrib.auth.decorators import login_required
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
import datetime


# 메인
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/article')
    else:
        return redirect('/sign-in')


# GET : 게시물 리스팅, 추천 컨텐츠 리스팅 / POST : 게시물 등록
def article(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        ### 데이터베이스에 있는 100개 드라마데이터 불러오기
        df = pd.read_csv('kdrama_encoded.csv')
        df1 = pd.read_csv('top100_kdrama.csv')

        try:
            ArticleList.objects.get(id=1)
        except:
            for i in range(0, len(df['Name'])):

                title = df['Name'][i]
                poster = f"Uploaded_Files/{title}.jpg"
                synopsis = df['Synopsis'][i]
                genre = df['Genre'][i]
                cast = df['Cast'][i]
                episode = df['Number of Episode'][i]
                tags = df['Tags'][i].split(',')
                aged = df['aged'][i]
                aired_date = df1['Aired Date'][i]

                article_list = ArticleList.objects.create(title=title, poster=poster, synopsis=synopsis, genre=genre,
                                                          aged=aged, aired_date=aired_date,
                                                          episode=episode, cast=cast, rating=0)
                for tag in tags:
                    tag = tag.strip()
                    if tag != '':  # 태그를 작성하지 않았을 경우에 저장하지 않기 위해서
                        article_list.tags.add(tag)

                article_list.save()
                ### 데이터베이스에 있는 100개 드라마데이터 불러오기
        all_article_list = ArticleList.objects.all()

        if user:
            all_article = ArticleList.objects.all()
            random_article = ArticleList.objects.order_by("?").first()

            my_preference = ArticleComment.objects.filter(author_id=request.user.id, rating=5)  # 사용자가 5점을 준 코멘트 가져오기
            if len(my_preference) != 0:  # 5점을 준 컨텐츠가 있을경우
                num = list(my_preference.values())  # article_id를 빼오기 위해 리스트화

                for i in num:
                    drama_num = i['article_id']

                content = ArticleList.objects.filter(id=drama_num)  # 사용자가 5점 준 comment.article_id에 해당하는 게시물 불러오기
                content = list(content.values())  # title을 빼오기 위해 리스트화
                for i in content:
                    title = i['title']

                df = pd.read_csv('kdrama_encoded.csv')
                name = list(df['Name'])

                drama_index = name.index(f'{title}')  # 사용자가 5점을 준 드라마의 csv파일안의 인덱스 빼오기

                for i in range(0, len(df['token'])):
                    df['token'][i] = df['token'][i].split(',')
                documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(df['token'])]
                model = Doc2Vec.load('static/models/content.model')

                inferred_doc_vec = model.infer_vector(df['token'][drama_index])  # 사용자가 5점 준 드라마와 비슷한 컨텐츠 뽑아오기
                # model.infer_vector(df['token'][int]) 함수에 넣어준 인덱스 값의 드라마 선택
                most_similar_docs = model.docvecs.most_similar([inferred_doc_vec], topn=5)

                for index, similarity in most_similar_docs:
                    print(f'{index}, similarity: {similarity}')
                    print(documents[index])

                index = []
                similarity = []
                for i in range(0, 5):
                    index.append(most_similar_docs[i][0] + 1)

                    similarity.append(most_similar_docs[i][1])
                ArticleRecomm.objects.all().delete()
                articles = ArticleList.objects.filter(id__in=index)

                return render(request, 'article/home.html', {'article': all_article, 'random_article': random_article,
                                                             'article_list': all_article_list,
                                                             'recommendation_list': index, 'recomm_articles': articles,
                                                             'similarity': similarity})
            else:
                return render(request, 'article/home.html', {'article': all_article, 'random_article': random_article,
                                                             'article_list': all_article_list})

        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        poster = request.FILES.get('poster', '')
        synopsis = request.POST.get('synopsis', '')
        genre = request.POST.get('genre', '')
        cast = request.POST.get('cast', '')
        aired_date = request.POST.get('aired_date', '')
        episode = request.POST.get('episode', '')
        aged = request.POST.get('aged', '')
        tags = request.POST.get('tags', '').split(',')

        my_article = ArticleList.objects.create(poster=poster, title=title, synopsis=synopsis,
                                                genre=genre,
                                                cast=cast, aired_date=aired_date, episode=episode, aged=aged, rating=0)

        for tag in tags:
            tag = tag.strip()
            if tag != '':  # 태그를 작성하지 않았을 경우에 저장하지 않기 위해서
                my_article.tags.add(tag)
        my_article.save()
        return redirect('/article')


# 게시물 상세페이지
@login_required
def detail_article(request, id):
    my_article = ArticleList.objects.get(id=id)
    article_comment = ArticleComment.objects.filter(article_id=id).order_by('-created_at')
    my_like = UserLike.objects.filter(user_id=request.user.id, article_id=id)
    return render(request, 'article/article_detail.html',
                  {'article': my_article, 'comment': article_comment, 'like': my_like})


# 댓글 등록
@login_required
def write_comment(request, id):
    if request.method == 'POST':
        current_article = ArticleList.objects.get(id=id)
        user = request.user
        my_comment = ArticleComment()
        my_comment.author = user
        my_comment.comment = request.POST.get('comment', '')
        my_comment.rating = int(request.POST.get('rating', ''))
        my_comment.article = current_article
        my_comment.save()

        comment_rating = ArticleComment.objects.filter(article_id=id)
        rate = 0
        if comment_rating:
            for rating in comment_rating:
                rate = rate + rating.rating
            current_article.rating = round(rate / len(comment_rating), 1)
        else:
            current_article.rating = rate
        current_article.save()

        return redirect('/article/' + str(id))


# 댓글 삭제
@login_required
def delete_comment(request, id):
    my_comment = ArticleComment.objects.get(id=id)
    my_comment.delete()

    current_article = ArticleList.objects.get(id=my_comment.article_id)
    comment_rating = ArticleComment.objects.filter(article_id=my_comment.article_id)
    rate = 0

    if comment_rating:
        for rating in comment_rating:
            rate = rate + rating.rating
        current_article.rating = round(rate / len(comment_rating), 1)
    else:
        current_article.rating = rate
    current_article.save()
    return redirect('/article/' + str(my_comment.article_id))


# 찜하기
@login_required
def like(request, id):
    me = request.user
    article = ArticleList.objects.get(id=id)
    my_like = UserLike.objects.filter(user_id=me.id, article_id=id)
    if my_like:
        my_like.delete()
    else:
        my_like = UserLike()
        my_like.article_id = article.id
        my_like.user_id = me.id
        my_like.save()

    return redirect('/article/' + str(id))


# 찜한 페이지 리스팅
def like_listing(request):
    me = request.user
    likes = UserLike.objects.filter(user_id=me.id)
    article = []
    for like in likes:
        article += ArticleList.objects.filter(id=like.article_id)
    return render(request, 'article/like.html', {'article': article})


# 검색 페이지 리스팅
def search(request):
    search = request.POST.get('search', '')
    my_search = ArticleList.objects.all().filter(title__contains=search)
    return render(request, 'article/search.html', {'article': my_search})


# 태그
class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = ArticleList

    def get_queryset(self):
        return ArticleList.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
