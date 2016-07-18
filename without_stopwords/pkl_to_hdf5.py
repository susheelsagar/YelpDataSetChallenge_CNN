__author__ = 's'

import cPickle,numpy,h5py

def convert_to_hdf5(x):
    #x = cPickle.load( open( "review_data/vector2.pkl", "rb" ) )
    f= open('/home/s/Desktop/CNN/review_data_without_stopwords/star_rating/stars_review.txt','r+')
    stars=[]
    for line in f:
        stars.append(float(line[0]))
    y = numpy.asarray(stars)
    train_count = 10000
    test_count = 2000
    s=(train_count,53,300)
    x_train = numpy.zeros(train_count*53*300).reshape(*s)
    y_train = numpy.zeros(train_count)
    s=(test_count,53,300)
    x_test = numpy.zeros(test_count*53*300).reshape(*s)
    y_test = numpy.zeros(test_count)
    i=0
    while i < train_count:
        j=0
        while j < 53:
            k=0
            while k < 300:
                x_train[i][j][k] = x[i][j][k]
                k=k+1
            j=j+1
        y_train[i] = y[i]
        i=i+1

    t=0
    while i<train_count+test_count:
        j=0
        while j<53:
            k=0
            while k<300:
                x_test[t][j][k] = x[i][j][k]
                k=k+1
            j=j+1
        y_test[t]=y[i]
        i=i+1
        t=t+1

    x_train = numpy.reshape(x_train,(train_count,1,53,300))
    y_train = numpy.reshape(y_train,(train_count,1))
    x_test = numpy.reshape(x_test,(test_count,1,53,300))
    y_test = numpy.reshape(y_test,(test_count,1))

    print "printing shapes of x_train,y_train,x_test,y_test"
    print x_train.shape,y_train.shape,x_test.shape,y_test.shape
    print "printing types of x and y"
    print type(x_train[0][0][0])
    print type(x_train[0][0][0][0]),y_train[0]

    with h5py.File('/home/s/Desktop/CNN/review_data_without_stopwords/h5_data_1/train_data.h5', 'w') as hf:
        hf.create_dataset('data', data=x_train)
        hf.create_dataset('label', data=y_train)
    with h5py.File('/home/s/Desktop/CNN/review_data_without_stopwords/h5_data_1/test_data.h5', 'w') as hf:
        hf.create_dataset('data', data=x_test)
        hf.create_dataset('label', data=y_test)







