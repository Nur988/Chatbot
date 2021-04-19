import re
import nltk
from nltk.corpus import wordnet

list_words=['job',' vacancy','hello','timings','location','price','schedule','manager','buy','business','services','product','problem','complain']
intent_list=['job','job','greet','time','location','price','schedule','manager','buy','business','services','product','problem','complain']
list_syn={} 
for word in list_words:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
   
    list_syn[word]=set(synonyms)
    
keywords={}
keywords_dict={}
for i in intent_list:

    keywords[i]=[]

# Defining a new key in the keywords dictionary

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for i in range(len(list_words)):
    for synonym in list(list_syn[list_words[i]]):
        keywords[intent_list[i]].append('.*\\b'+synonym+'\\b.*')
 

for intent, keys in keywords.items():
    
    # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
    keywords_dict[intent]=re.compile('|'.join(keys))


#defining responses

responses={
    'greet':'Hello! How can I help you sir?',
    'time':'We are open from 10AM to 6PM, Monday to Friday. We are closed on weekends and public holidays.',
    'fallback':'I dont quite understand. Could you repeat that?',
    'location':"We are located in House 87-89, Road 4, Block B, Niketan 1212 Dhaka, Dhaka Division, Bangladesh",
    'price':'You can find the details at our website',
    'schedule':"The event starts at 6pm",
    'buy':"You can get datails at our website ",
    'services':"We provide a range of tech and marketing services",
    'product':"Our products are listed in the Website",
    'problem':"For any queries call us",
    'complain':"For complains please call us",
    'job':"We regularly post about vacancies in our facebook page. Please keep an eye on our facebook pageto get further updates."


}


