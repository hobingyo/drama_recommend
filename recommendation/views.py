from django.shortcuts import render
import MeCab
from gensim.test.utils import common_texts
import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


# 설치해야할 것들
# !pip install mecab-python3
# !pip install unidic-lite
# !pip install --no-binary :all: mecab-python3



def content_recommendation(int):
    df = pd.read_csv('../kdrama_encoded.csv')
    for i in range(0, len(df['token'])):
        df['token'][i] = df['token'][i].split(',')
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(df['token'])]
    model = Doc2Vec.load('../static/models/content.model')

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


    # 프린트 인덱스까지는 되는데

    return index, similarity

