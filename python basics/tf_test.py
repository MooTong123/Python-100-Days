# -- coding: utf-8 --
# import os
import tensorflow as tf
import numpy as np
import jieba
from collections import defaultdict
from gensim import corpora, models, similarities
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def test_tensorflow():
    print('\ntest tensorflow 1,14,0-----------------------------')
    a = tf.constant([1.0, 2.0], name='a')
    b = tf.constant([2.0, 3.0], name='b')
    result = a + b
    sess = tf.compat.v1.Session()
    print(sess.run(result))

def test_jieba():
    print('\ntest jieba -----------------------------')
    text1 = '中华人民共和国是一个伟大国家'
    words = ' '.join(jieba.cut(text1, cut_all=True))
    print(words)

def test_numpy():
    print('\ntest numpy -----------------------------')
    x = np.random.random(10)  # >0.5
    y = np.random.random(10) > 0.5
    print(x, y)

    x = np.asarray(x, np.int32)
    y = np.asarray(y, np.int32)
    print(x, y)

def test_gensim():
    print('\ntest gensim -----------------------------')
    documents = ["Human machine interface for lab abc computer applications",
                 "A survey of user opinion of computer system response time",
                 "The EPS user interface management system",
                 "System and human system engineering testing of EPS",
                 "Relation of user perceived response time to error measurement",
                 "The generation of random binary unordered trees",
                 "The intersection graph of paths in trees",
                 "Graph minors IV Widths of trees and well quasi ordering",
                 "Graph minors A survey"]

    stoplist = set('for a of the and to in'.split())
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]  # 遍历文档并分词

    print(texts)

    # 2.计算词频
    frequency = defaultdict(int)  # 构建一个字典对象
    # 遍历分词后的结果集，计算每个词出现的频率
    for text in texts:
        for token in text:
            frequency[token] += 1
    # 选择频率大于1的词
    texts = [[token for token in text if frequency[token] > 1] for text in texts]

    print(texts)

    # 3.创建字典（单词与编号之间的映射）
    dictionary = corpora.Dictionary(texts)
    # print(dictionary)
    # Dictionary(12 unique tokens: ['time', 'computer', 'graph', 'minors', 'trees']...)
    # 打印字典，key为单词，value为单词的编号
    print(dictionary.token2id)
    # {'human': 0, 'interface': 1, 'computer': 2, 'survey': 3, 'user': 4, 'system': 5, 'response': 6, 'time': 7, 'eps': 8, 'trees': 9, 'graph': 10, 'minors': 11}

    # 4.将要比较的文档转换为向量（词袋表示方法）
    # 要比较的文档
    new_doc = "Human computer interaction"
    # 将文档分词并使用doc2bow方法对每个不同单词的词频进行了统计，并将单词转换为其编号，然后以稀疏向量的形式返回结果
    new_vec = dictionary.doc2bow(new_doc.lower().split())
    # print(new_vec)

    # 5.建立语料库
    # 将每一篇文档转换为向量
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(corpus)

    # 6.初始化模型
    # 初始化一个tfidf模型,可以用它来转换向量（词袋整数计数）表示方法为新的表示方法（Tfidf 实数权重）
    tfidf = models.TfidfModel(corpus)
    # 测试
    test_doc_bow = [(0, 1), (1, 1)]
    print(tfidf[test_doc_bow])
    # [(0, 0.7071067811865476), (1, 0.7071067811865476)]

    # 将整个语料库转为tfidf表示方法
    corpus_tfidf = tfidf[corpus]
    for doc in corpus_tfidf:
        print(doc)

    # 7.创建索引
    index = similarities.MatrixSimilarity(corpus_tfidf)

    # 8.相似度计算
    new_vec_tfidf = tfidf[new_vec]  # 将要比较文档转换为tfidf表示方法
    print(new_vec_tfidf)
    # [(0, 0.7071067811865476), (2, 0.7071067811865476)]

    # 计算要比较的文档与语料库中每篇文档的相似度
    sims = index[new_vec_tfidf]
    print(sims)
    # [ 0.81649655  0.31412902  0.          0.34777319  0.          0.          0.
    #  0.          0.        ]

if __name__ == '__main__':
    test_tensorflow()
    test_jieba()
    test_numpy()
    test_gensim()