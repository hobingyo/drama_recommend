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
    df = pd.read_csv('top100_kdrama_ko.csv')

    mecab = MeCab.Tagger("-Owakati")
    mecab.parse("kill bill").split()
    test = mecab.parse(df['Synopsis'][0]).split()

    df['token'] = 0
    for i in range(0, len(df['Genre'])):
        df['token'][i] = mecab.parse(df['Genre'][i]).split()
        df['token'][i].extend(mecab.parse(df['Tags'][i]).split())

    # 유사도와 상관없을 것 같은 요소 제거해주기
    list1 = [',', '.', 's', "'", '"', '-', '…', '(', ')', '년']

    for j in list1:
        for i in range(0, len(df['token'])):
            while j in df['token'][i]:
                df['token'][i].remove(j)

    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(df['token'])]
    model = Doc2Vec(documents, vector_size=100, window=3, epochs=10, min_count=0, workers=4)
    inferred_doc_vec = model.infer_vector(df['token'][int])
    # model.infer_vector(df['token'][int]) 함수에 넣어준 인덱스 값의 드라마 선택
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

