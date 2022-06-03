from django.shortcuts import render

import MeCab
import pandas as pd
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


# 설치해야할 것들
# !pip install mecab-python3
# !pip install unidic-lite
# !pip install --no-binary :all: mecab-python3


def content_recommendation(int):
    df = pd.read_csv('../top100_kdrama.csv')

    mecab = MeCab.Tagger("-Owakati")
    mecab.parse("kill bill").split()
    test = mecab.parse(df['Synopsis'][0]).split()

    df['token'] = 0
    for i in range(0, len(df['Genre'])):
        df['token'][i] = mecab.parse(df['Genre'][i]).split()
        df['token'][i].extend(mecab.parse(df['Tags'][i]).split())

    # 유사도와 상관없을 것 같은 단어 제거해주기, 영어보다 한글단어가 더 정확도가 높을 것 같다.
    # 한글과 달리, 영어로 이름을 표기하면 글자 하나하나의 유사도를 찾아서 의도와 다른 분석이 됨.
    list1 = ['From', 'A', 'The', 'In', 'is', 'a', 'to', 'To', 'by', ',', '.', 's', "'", '"', '-', 'The', 'of',
             'their',
             'but', 'and', 'that', 'are', 'at', 'the', 'in', 'have', 'who', 'as', 'he', 'his', 'she', 'her', 'they',
             'their']

    for j in list1:
        for i in range(0, len(df['token'])):
            while j in df['token'][i]:
                df['token'][i].remove(j)

    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(df['token'])]
    model = Doc2Vec(documents, vector_size=100, window=3, epochs=10, min_count=0, workers=4)
    inferred_doc_vec = model.infer_vector(df['token'][int])
    most_similar_docs = model.docvecs.most_similar([inferred_doc_vec], topn=10)

    for index, similarity in most_similar_docs:
        print(f'{index}, similarity: {similarity}')
        print(documents[index])

    index = []
    similarity = []
    for i in range(0, 10):
        index.append(most_similar_docs[i][0])
        similarity.append(most_similar_docs[i][1])

    return index, similarity

