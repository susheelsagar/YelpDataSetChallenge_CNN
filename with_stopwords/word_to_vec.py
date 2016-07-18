__author__ = 's'

import gensim,os,numpy,cPickle
from pkl_to_hdf5 import convert_to_hdf5

class MySentences(object):

     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 yield line.split()

def word2vec():
    i=0
    print "Entered word2vec"
    sentences = MySentences('/home/s/Desktop/CNN/review_data_with_stopwords_10k/text_review') # a memory-friendly iterator
    print "number of reviews = ",
    for line in sentences:
        i=i+1
    print i
    i=0
    for line in sentences:
        i=i+1
    print i
    print "training started"
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
    convert_to_hdf5(x_train)
