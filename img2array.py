# This script is used for reading png files and storing them in form of numpy array to file

import numpy as np
import cv2
import sys

# Define a variables to store training image data and the training labels
# train_data_X = np.zeros((1,3072))
num_examples = 1000


# Saving train data
count = 1
for j in range(1,51):
    train_data_X = np.zeros((1,3072))
    for i in range(num_examples):
        img_file = '../train/'+str(count)+'.png'
        count += 1
        print img_file
        # read the image
        im = cv2.imread(img_file)
        # try converting image to double if this does not give a good result
        # flatten and append    #any of this function might be useful --> concatenate((a,b)) or vstack((a,b)) or r_[a,b]
        train_data_X = np.vstack((train_data_X,im.flatten(1)))
    
    filename = '../train_data/train_data_'+str(j)+'.npy'
    np.save(filename,train_data_X[1:,:])
    del train_data_X
    print filename + " saved successfully!"

# Data Saved
print "train data saved!"

sys.exit(0)

# Saving test data
count = 1
for j in range(1,301):
    test_data_X = np.zeros((1,3072))
    for i in range(num_examples):
        img_file = '../test/'+str(count)+'.png'
        count += 1
        print img_file
        # read the image
        im = cv2.imread(img_file)
        # try converting image to double if this does not give a good result
        # flatten and append    #any of this function might be useful --> concatenate((a,b)) or vstack((a,b)) or r_[a,b]
        train_data_X = np.vstack((test_data_X,im.flatten(1)))
    
    filename = '../test_data/test_data_'+str(j)+'.npy'
    np.save(filename,test_data_X[1:,:])
    del test_data_X
    print filename + " saved successfully!"

# Data Saved
print "test data saved!"