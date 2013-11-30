# This script is used for reading png files and storing them in form of numpy array to file

import numpy as np
import cv2
import sys

# Define a variables to store training image data and the training labels
# train_data_X = np.zeros((1,3072))
num_examples = 500
dim = 3072

# Saving train data
count = 1
for j in range(1,101):
    train_data_X = np.zeros((1,dim))
    for i in range(num_examples):
        img_file = '../train/'+str(count)+'.png'
        count += 1
        print img_file
        # read the image
        im = cv2.imread(img_file)
        #gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        #sx = np.uint8(np.absolute(cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)))
        #sy = np.uint8(np.absolute(cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)))
        # try converting image to double if this does not give a good result
        # flatten and append    #any of this function might be useful --> concatenate((a,b)) or vstack((a,b)) or r_[a,b]
        #train_data_X = np.vstack((train_data_X,np.hstack((np.hstack((im.flatten(1),sx.flatten(1))),sy.flatten(1)))))
        train_data_X = np.vstack((train_data_X,im.flatten(1)))
        
        
    filename = '../train_data/train_data_'+str(j)+'.npy'
    np.save(filename,train_data_X[1:,:])
    del train_data_X
    print filename + " saved successfully!"

# Data Saved
print "train data saved!"


num_examples = 500
# Saving test data
count = 1
for j in range(1,601):
    test_data_X = np.zeros((1,dim))
    for i in range(num_examples):
        img_file = '../test/'+str(count)+'.png'
        count += 1
        print img_file
        # read the image
        im = cv2.imread(img_file)
        #gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        #sx = np.uint8(np.absolute(cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)))
        #sy = np.uint8(np.absolute(cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)))
        # try converting image to double if this does not give a good result
        # flatten and append    #any of this function might be useful --> concatenate((a,b)) or vstack((a,b)) or r_[a,b]
        #test_data_X = np.vstack((test_data_X,np.hstack((np.hstack((im.flatten(1),sx.flatten(1))),sy.flatten(1)))))
        test_data_X = np.vstack((test_data_X,im.flatten(1)))
        
        
    filename = '../test_data/test_data_'+str(j)+'.npy'
    np.save(filename,test_data_X[1:,:])
    del test_data_X
    print filename + " saved successfully!"

# Data Saved
print "test data saved!"