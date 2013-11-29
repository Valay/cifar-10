import numpy as np
from sklearn.ensemble import RandomForestClassifier
import cv2
import json
import pickle

# Define a variables to store training image data and the training labels

# Load the labels
with open('IntsToLabels.json','r') as f:
    i2l = json.load(f)   # i2l = Integers to Labels

with open('LabelsToInts.json','r') as f:
    l2i = json.load(f)   # l2i = Labels to Integers


# Load an test the model on the the test set
#num_test_examples = 3000

# get the model
with open('model.pkl','rb') as f:
     clf = pickle.load(f)
print "Model Loaded!"
     
     
with open('../testSubmission.csv','w') as f:
    f.write('id'+','+'Label\n')

num_examples = 500   # images in one test_data_i file

count = 1
print "Loading Test Data"
for i in range(1,601):
    filename = '../test_data/test_data_'+str(i)+'.npy'
    test_data_X = np.load(filename)  # load the data from file train_data.npy
    #test_data_X = np.vstack((test_data_X,data))

    ytest = clf.predict(test_data_X)
    del test_data_X   # No need to save test_data_X as it will get replaced next time

    print "Writing Labels to file for %d file!" % i
    # dump the labels to file
    with open('../testSubmission.csv','a') as f:
        for i in range(num_examples):
            line = str(count)+','+i2l[str(ytest[i])]+'\n'
            count += 1
            f.write(line)