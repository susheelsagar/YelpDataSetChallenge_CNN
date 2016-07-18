__author__ = 's'
import gensim,os,numpy,json,sknn,cPickle
from sknn.mlp import Convolution,Layer,Classifier


class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 yield line.split()


sentences = MySentences('/home/s/Desktop/reviews/') # a memory-friendly iterator

model = gensim.models.Word2Vec.load_word2vec_format('/home/s/Desktop/GoogleNews-vectors-negative300.bin',binary=True)
print 'training done'
model.build_vocab(sentences)
model.train(sentences)

vector = []
for line in sentences:
   line_vector = []
   k=0
   while k<len(line):
       try :
           line_vector.append(model[line[k]])
       except Exception, err :
            line_vector.append(numpy.zeros(300,dtype=float))
       k= k+1
   while k<53:
       line_vector.append(numpy.zeros(300,dtype=float))
       k=k+1
   vector.append(line_vector)

x_train = numpy.asarray(vector)
print x_train.shape,type(x_train)
'''
f= open('stars_review.txt','r+')
stars = []
for line in f:
    stars.append(line[0])
y_train = numpy.asarray(stars)
#print y_train.shape,type(y_train)


#cPickle.dump( x_train, open( "vector2.pkl", "wb" ) )
x_train = cPickle.load( open( "vector2.pkl", "rb" ) )

print x_train.shape,y_train.shape,type(x_train),type(y_train)
print x_train[0][5]

layer1 = Convolution('Rectifier',kernel_shape=(5,4),channels=50,kernel_stride=2,pool_shape=(2,2),pool_type='max',weight_decay=0.0005,dropout=0.5,)
layer2 = Convolution('Rectifier',kernel_shape=(6,5),channels=100,kernel_stride=2,pool_shape=(2,2),pool_type='max',weight_decay=0.0005,dropout=0.5,)
layer3 = Convolution('Rectifier',kernel_shape=(6,5),channels=100,kernel_stride=2,pool_shape=(2,2),pool_type='max',weight_decay=0.0005,dropout=0.5,)
layer4 = Layer('Softmax')
layers = [layer1,layer3,layer4]

nn = Classifier(layers,learning_rule='sgd',learning_rate=0.001,learning_momentum=0.9,regularize='L1',batch_size=10,weight_decay=0.0005,dropout_rate=0.5,n_iter=10,loss_type='mcc')
nn.fit(x_train , y_train)

print nn.predict(x_train)'''






'''f = open('vector2','r+')
i=0
while i<vector.__len__():
    j=0
    while j<len(vector[i]):
        k=0
        while k<len(vector[i][j]):
            f.write(str(vector[i][j][k]))
            f.write(' ')
            k=k+1
            print i,j,k
        f.write('\n')
        j=j+1;
    f.write('&&\n')
    i=i+1'''

'''model = gensim.models.Word2Vec(sentences,min_count=1,workers=4)'''


'''data = []
i=0

    with open('/home/s/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json') as infile:
    for line in infile:
        if(i>100):
            break
        sentence = []
        data.append(json.loads(line))
        count = data[i]['text'].split()
        k=0;
        while k<len(count):
            sentence.append(model[count[k]])
            k=k+1;
        data.append(sentence[0])
        i=i+1;'''
