

from nltk.stem import PorterStemmer

lemm=PorterStemmer()
keywords=[]
keywords.append(['job','vacancy'])
keywords.append(['talk','speak','contact','agent'])
keywords.append(['call','message','email'])
keywords.append(['requirement','help','assist','recommend'])
keywords.append(['offer','package','scheme'])
keywords.append(['hire','work'])
keywords.append(['internship','intern','trainee','training'])
keywords.append(['hello','how','hi','howdy','good morning',])
for i in keywords:
    for j in range(len(i)):
        
        i[j]=lemm.stem(i[j])