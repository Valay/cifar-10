import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
import cv2

# Define a variable to store image data
train_data_X = np.zeros((1,3072))

# Load the data
for i in range(1,1000):
    img_file = '../train/'+str(i)+'.png'
    print img_file
    # read the image
    im = cv2.imread(img_file)
    # try converting image to double if this does not give a good result
    # flatten and append    #any of this function might be useful --> concatenate((a,b)) or vstack((a,b)) or r_[a,b]
    train_data_X = np.vstack((train_data_X,im.flatten(1)))


clf = RandomForestClassifier(n_jobs=2)
clf.fit(train[features], y)