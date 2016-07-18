__author__ = 's'

# Reading the reviews from a json file and removing the stopwords from each review.
# Loading the reviews with number of words less that 53 into a text file

import json
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def filter_store(k) :
    print "printing in filter_store"
    tokenizer = RegexpTokenizer(r'\w+')
    data = []
    stars = []
    i=0
    with open(k) as infile :
        for line in infile:
            l = json.loads(line)
            tokens = None
            try:
                text = str(l['text'])
                tokens = tokenizer.tokenize(l['text'])
                if len(tokens)>53:
                    continue
            except Exception,err:
                continue
            rating = l['stars']
            filtered_words = None
            filtered_words = [word for word in tokens if word not in stopwords.words('english')]
            data.append(filtered_words)
            stars.append(rating)
            i=i+1
            if i==24000 :
                break
    i=0
    count =0;
    f= open('/home/s/Desktop/CNN/review_data_without_stopwords/text_review/text_review.txt','r+')
    f1=open('/home/s/Desktop/CNN/review_data_without_stopwords/star_rating/stars_review.txt','r+')
    while i<len(data):
        k=0
        while k<len(data[i]):
            try:
                review = str(data[i][k]+ ' ')
                f.write(review)
                k=k+1
            except Exception,err:
                print '*********************************************************************************'
                k=k+1
        f.write('\n')
        f1.write(str(stars[i]))
        f1.write('\n')
        i=i+1
    print "end of filter_store"
    print i

