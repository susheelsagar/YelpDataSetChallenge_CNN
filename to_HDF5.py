__author__ = 's'
import cPickle,numpy,h5py

x_train = cPickle.load( open( "vector2.pkl", "rb" ) )
f= open('stars_review.txt','r+')
stars=[]
for line in f:
    stars.append(float(line[0]))
y_train = numpy.asarray(stars)
s= (50,53,300)
x_test = numpy.zeros(795000).reshape(*s)
y_test = numpy.zeros(50)
x_val = numpy.zeros(795000).reshape(*s)
y_val = numpy.zeros(50)
i=0
while i<50:
    j=0
    while j<53:
        k=0
        while k<300:
            x_test[i][j][k] = x_train[i][j][k]
            k=k+1
        j=j+1
    y_test[i] = y_train[i]
    i=i+1
l=0
while i<100:
    j=0
    while j<53:
        k=0
        while k<300:
            x_val[l][j][k] = x_train[i][j][k]
            k=k+1
        j=j+1
    y_val[l] = y_train[i]
    i=i+1
    l=l+1

'''print x_test.shape,type(x_test),y_test.shape,type(y_test)
print x_val.shape,type(x_val),y_val.shape,type(y_val)
print x_train.shape, y_train.shape'''
x_train = numpy.reshape(x_train,(200,1,53,300))
y_train = numpy.reshape(y_train,(200,1))
x_test = numpy.reshape(x_test,(50,1,53,300))
y_test = numpy.reshape(y_test,(50,1))
print x_train.shape,y_train.shape,x_test.shape,y_test.shape

print type(x_train[0][0][0])
print type(x_train[0][0][0][0]),y_train[0]

with h5py.File('temp/train_data.h5', 'w') as hf:
    hf.create_dataset('data', data=x_train)
    hf.create_dataset('label', data=y_train)
with h5py.File('temp/test_data.h5', 'w') as hf:
    hf.create_dataset('data', data=x_test)
    hf.create_dataset('label', data=y_test)
with h5py.File('temp/val_data.h5', 'w') as hf:
    hf.create_dataset('data', data=x_val)
    hf.create_dataset('label', data=y_val)

