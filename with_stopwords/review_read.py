__author__ = 's'
import json
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def filter_store(k):
    print "printing in filter_store"
    tokenizer = RegexpTokenizer(r'\w+')
    data = []
    stars = []
    i=0
    f = open('text','r+')
    with open(k) as infile:
        for line in infile:
            text = None
            l= json.loads(line)
            rating = l['stars']
            try:
                text = str(l['text'])
                tokens = tokenizer.tokenize(l['text'])

            except Exception,err:
                continue
            text = text.split()
            if(len(text)<54):
                print tokens
                data.append(tokens)
                stars.append(rating)
                i=i+1
            if(i==12000):
                break
    i = 0
    count = 0

    f = open('/home/s/Desktop/CNN/review_data_with_stopwords/text_review/text_review.txt','r+')
    f1 = open('/home/s/Desktop/CNN/review_data_with_stopwords/star_rating/stars_review.txt','r+')
    while i<len(data):
        k=0
        while k< len(data[i]):
            try:
                review = str(data[i][k]+ ' ')
                f.write(review)
                k= k+1
            except Exception,err:
                k=k+1
        f.write('\n')
        f1.write(str(stars[i]))
        f1.write('\n')
        i=i+1
    print 'end of filter_store'
    print i




