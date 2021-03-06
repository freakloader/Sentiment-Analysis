from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score as ACC
from sklearn import svm as SVM
#import numpy as np
from Dataprocessing import words
import pickle as pkl

#For 1600 review data (78-79 percent accuracy)
##f=open('1600train.pkl','rb')
##train=pkl.load(f)
##f.close()

##f=open('1600test.pkl','rb')
##test=pkl.load(f)
##f.close()

#For 10000 review data (87-88 percent accuracy)
f=open('10000train.pkl','rb')
train=pkl.load(f)
f.close()

f=open('10000test.pkl','rb')
test=pkl.load(f)
f.close()

#For 25000 review data (87-88 percent accuracy)
#f=open('25000train.pkl','rb')
##train=pkl.load(f)
##f.close()

##f=open('25000test.pkl','rb')
##test=pkl.load(f)
##f.close()

#print(type(train[0]))

vect=TfidfVectorizer()

trainfeat=vect.fit_transform(train[0])
testfeat=vect.transform(test[0])
#print(type(testfeat))
#print(trainfeat.shape)
#print(len(train[1]))
svm=SVM.LinearSVC()
svm.fit(trainfeat,train[1])
predict=svm.predict(testfeat)
#print(predict)
#print(type(predict))

print("Accuracy:-{ACC}%".format(ACC=100*ACC(test[1],predict)))

while True:
    review=[]
    line=input("Enter a sentence('Quit' to quit):\n")
    if line!='Quit':
        #print("Words Type:"+type(review).__name__)
        review.append(line)
        #print(review)
        #a=words(review)
        #print(a)
        #print("Words Type:"+type(a).__name__)
        data=vect.transform(words(review))
        #print(data)
        #print(type(data))
        predict=svm.predict(data)
        #print(predict)
        #print("Predict 0:"+np.array2string(predict[0]))
        if(predict==1):
            print("POSITIVE\n")
        else:
            print("NEGATIVE\n")
    elif line == 'Quit':
        break
