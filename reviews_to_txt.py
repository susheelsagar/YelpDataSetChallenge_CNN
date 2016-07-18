__author__ = 's'
import json
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

import nltk


f = open('/home/s/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json','r+')
f2=open('text_review.txt',"r+")
f3=open('stars_review.txt',"r+")
tokenizer = RegexpTokenizer(r'\w+')
data = []
i=0
count =0
ma=0
length_tokens = []
with open('/home/s/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json') as infile:
    for line in infile:
        if(i==10000):
            break
        data.append(json.loads(line))
        text = data[i]['text']
        stars = str(data[i]['stars'])
        tokens = tokenizer.tokenize(text)
        #tags = nltk.pos_tag(tokens)
        '''k=0
        count =0;
        while k<tags.__len__():
            if tags[k][1]!='IN'  :
                #print tags[k]
                count =count+1;
            k=k+1'''
        filtered_words = None
        filtered_words = [word for word in tokens if word not in stopwords.words('english') ]

        count = count+len(filtered_words)
        if ma<len(filtered_words):
            ma = len(filtered_words)
        #print count,data[i]['stars']

        '''
        f2.write(text.encode('utf8')+'\n')
        f3.write(stars.encode('utf8')+'\n')'''
        i=i+1
        if(i%1000==0): print i
print '\n',count/i,count,i,ma