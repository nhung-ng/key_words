import processing
import re
from underthesea import word_tokenize, pos_tag
from gensim import models, corpora
import logging
from gensim.models.ldamodel import LdaModel
import sys


#Get data and text lower
input_file=sys.argv[1]
data=[]
with open(input_file,'r+',encoding='utf-8') as fr:
    for text in fr:
        text = text.lower()
        data.append(text)

stopwords =set()
with open("stopwords.txt","r",encoding="utf-8") as f:
    stopwords = f.read().split("\n")

#token and cleaning text
texts_clean = processing.text_preprocess(data)


#remove stopwords
texts_words =[]
for line in texts_clean:
    text =[]
    line=(list(line.split()))
    for w in line:
        if w not in stopwords:
            text.append(w)
    texts_words.append(text)

id2word = corpora.Dictionary(texts_words)

corpus =[]
for text in texts_words:
    new = id2word.doc2bow(text)
    corpus.append(new)

lda_model = LdaModel(corpus=corpus,
                    id2word=id2word,
                   num_topics=10,
                   random_state=100,
                   update_every=1,
                   chunksize=100,
                   passes=0,
                   alpha="auto")

#topics_file
result=sys.argv[2]
with open(result, 'w',encoding="utf-8") as rf:
    topics=lda_model.top_topics(corpus)
    rf.write('\n'.join('%s %s' %topic for topic in topics))

#from pprint import pprint
#pprint(lda_model.print_topics())
