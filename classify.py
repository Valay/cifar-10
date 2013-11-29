import numpy as np
from sklearn.ensemble import RandomForestClassifier
import cv2
import json

# Define a variables to store training image data and the training labels

# Load the labels
with open('IntsToLabels.json','r') as f:
    i2l = json.load(f)   # i2l = Integers to Labels

with open('LabelsToInts.json','r') as f:
    l2i = json.load(f)   # l2i = Labels to Integers


# Load the test set
#num_test_examples = 3000
test_data_X = np.zeros((1,3072))
print "Loading Test Data"
# Load the test data
for i in range(1:301):
    filename = '../test_data/test_data_'+str(i)+'.npy'
    data = np.load(filename)  # load the data from file train_data.npy
    test_data_X = np.vstack((test_data_X,data))
    del data
print "Test data loaded\n"

print "Testing model"
# Test the model
ytest = clf.predict(test_data_X[1:,:])
print "model tested\n"

print "Writing Labels to file"
# dump the labels to file
# with open('../testSubmission.csv','a') as f:
#     f.write('id'+','+'Label\n')
#     for i in range(num_examples):
#         line = str(i+1)+','+i2l[str(ytest[i])]+'\n'
#         f.write(line)