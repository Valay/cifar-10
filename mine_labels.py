# This script is used to conver the labels to integer values so that it can be used by any classifier

# fp = open('../trainLablesIntegers.csv','a')

import json

Label_dict = {
    'horse' : 1,
    'ship' : 2,
    'cat' : 3,
    'frog' : 4,
    'truck' : 5,
    'deer' : 6,
    'bird' : 7,
    'automobile' : 8,
    'airplane' : 9,
    'dog' : 10
}

Label_rev = {}

for key in Label_dict.keys():
    Label_rev[Label_dict[key]] = key
    
print Label_dict
print Label_rev

with open('LablesToInts.json','w') as f:    
    json.dump(Label_dict,f)
with open('IntsToLables.json','w') as f: 
    json.dump(Label_rev,f) 

with open('../trainLabels.csv') as f:
    for line in f:
        words = line.split(',')
        #print words[0], words[1]
        words[1] = words[1].strip()
        fp.write( str(words[0]) + ',' + str(Label_dict[words[1]])+'\n' ) 

# Great Labels mined Successfully!    