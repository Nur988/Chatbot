def preprocess(usertext):
    #from nltk.stem import PorterStemmer

    #lemm=PorterStemmer()

    
    usertext=usertext.split(' ')
    for i in range(len(usertext)):
        usertext[i]=usertext[i].lower()
    #for i in range(len(usertext)):
       # usertext[i]=lemm.stem(usertext[i])

    return usertext       



