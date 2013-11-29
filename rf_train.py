import numpy as np
from sklearn.ensemble import RandomForestClassifier
import cv2
import json
import pickle

# Define a variables to store training image data and the training labels
train_data_X = np.zeros((1,3072))
num_examples = 50000
y = np.zeros((num_examples),dtype='uint8')

# Load the labels and conversion
with open('IntsToLabels.json','r') as f:
    i2l = json.load(f)   # i2l = Integers to Labels

with open('LabelsToInts.json','r') as f:
    l2i = json.load(f)   # l2i = Labels to Integers

# Load the training data
print "Loading Train images!"
for i in range(1,51):
    filename = '../train_data/train_data_'+str(i)+'.npy'
    data = np.load(filename)  # load the data from file train_data.npy
    train_data_X = np.vstack((train_data_X,data))
    del data
print "Train images loaded! \n"

# Load the labels # Obselete code
# with open('../trainLabelsIntegers.csv','r') as f:
#     for i in range(num_examples):
#         line = f.readline()
#         words = line.split(',')
#         #print i, int(words[1].strip())
#         y[i] = int(words[1].strip())

# Load the Train Labels
print "Loading train Labels"
with open('../trainLabels.csv','r') as f:
    for i in range(num_examples):
        line = f.readline()
        words = line.split(',')
        #print i, int(words[1].strip())
        y[i] = l2i[words[1].strip()]
print "Train labels loaded! \n"

print "Training Model"
# Train the classifier
clf = RandomForestClassifier(n_jobs=2)
clf.fit(train_data_X[1:,:], y)    # Change this!
# del train_data_X
# del y

# save the model
with open('model.pkl','w') as f:
    pickle.dump(clf,f)
print "Model trained and saved\n"


print "Testing model on train data!"
# Testing on train set
ytrain = clf.predict(train_data_X[40001:,:])

print ytrain.shape, train_data_X.shape, y.shape
count = 0
for i in range(10000):
    if ytrain[i] != y[i+40000]:
        count = count+1
    #print ytrain[i], y[i+40000]

print count            
# print 'train_error is %d' % (float(count)/10000)
# Finish this function