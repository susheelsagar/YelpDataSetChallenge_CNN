__author__ = 's'
import json
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+')
data = []
stars=[]
i=0;
with open('/home/s/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json') as infile:
        for line in infile:
            l = json.loads(line)
            rating = l['stars']
            tokens = tokenizer.tokenize(l['text'])
            filtered_words = None
            filtered_words = [word for word in tokens if word not in stopwords.words('english') ]
            if len(filtered_words) < 54:
                data.append(filtered_words)
                stars.append(rating)
                i=i+1
            if(i%10==0): print i,
            if i==200 :
                break
i=0
count =0;
f= open('text_review.txt','r+')
f1=open('stars_review.txt','r+')
while i<len(data):
    k=0
    while k<len(data[i]):
        f.write(data[i][k]+' ')
        k=k+1
    count=count+k
    f.write('\n')
    f1.write(str(stars[i]))
    f1.write('\n')
    i=i+1
print count
