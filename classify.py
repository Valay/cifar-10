import numpy as np
from sklearn.ensemble import RandomForestClassifier
import cv2
import json

# Define a variables to store training image data and the training labels
train_data_X = np.zeros((1,3072))
num_examples = 2000
y = np.zeros((num_examples),dtype='uint8')

with open('IntsToLabels.json','r') as f:
    i2l = json.load(f)   # i2l = Integers to Labels

with open('LabelsToInts.json','r') as f:
    l2i = json.load(f)   # l2i = Labels to Integers

print "Loading Train images!"
# Load the training data
for i in range(num_examples):
    img_file = '../train/'+str(i+1)+'.png'
    print img_file
    # read the image
    im = cv2.imread(img_file)
    # try converting image to double if this does not give a good result
    # flatten and append    #any of this function might be useful --> concatenate((a,b)) or vstack((a,b)) or r_[a,b]
    train_data_X = np.vstack((train_data_X,im.flatten(1)))

print "test images loaded! \n"
# Load the labels
# with open('../trainLabelsIntegers.csv','r') as f:
#     for i in range(num_examples):
#         line = f.readline()
#         words = line.split(',')
#         #print i, int(words[1].strip())
#         y[i] = int(words[1].strip())

print "Loading train Labels"
# Load the Labels
with open('../trainLabels.csv','r') as f:
    for i in range(num_examples):
        line = f.readline()
        words = line.split(',')
        #print i, int(words[1].strip())
        y[i] = l2i[words[1].strip()]
print "labels loaded! \n"

print "Training Model"
# Train the classifier
clf = RandomForestClassifier(n_jobs=2)
clf.fit(train_data_X[1:,:], y)

print "model trained\n"
# Test the classifier on training data (to get train error)
# ytrain = clf.predict(train_data_X[1:,:])
# count = 0
# for i in range(999):
#     if ytrain[i+1] != y[i]:
#         count = count+1
#             
# print 'train_error is %d' % float(count/num_examples)

num_test_examples = 3000
test_data_X = np.zeros((1,3072))

print "Loading Test Data"
# Load the test data
# for i in range(num_test_examples):
#     img_file = '../test/'+str(i+1)+'.png'
#     print img_file
#     # read the image
#     im = cv2.imread(img_file)
#     # try converting image to double if this does not give a good result
#     # flatten and append    #any of this function might be useful --> concatenate((a,b)) or vstack((a,b)) or r_[a,b]
#     test_data_X = np.vstack((test_data_X,im.flatten(1)))

print "test data loaded\n"

print "testing model"
# Test the model


# Testing on a different set of the test data
ytrain = clf.predict(train_data_X[1001:,:])
a = np.nonzero(ytrain - y[1000:])
print a
count = 0
for i in range(1000):
    if ytrain[i] != y[i+1000]:
        count = count+1
# import pdb
# pdb.set_trace()
            
print 'train_error is %d' % (float(count)/num_examples)

# ytest = clf.predict(test_data_X[1:,:])
print "model tested\n"

print "Writing Labels to file"
# dump the labels to file
# with open('../testSubmission.csv','a') as f:
#     f.write('id'+','+'Label\n')
#     for i in range(num_examples):
#         line = str(i+1)+','+i2l[str(ytest[i])]+'\n'
#         f.write(line)