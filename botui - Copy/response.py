from chatbot import keywords_dict
from chatbot import responses
import re

class Response:
    def __init__(self,input):
        self.i=input
        



    def output(self):
        user_input= self.i
        matched_intent=None
        for intent,pattern in keywords_dict.items():
        
        # Using the regular expression search function to look for keywords in user input
            if re.search(pattern, user_input): 
            
        # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
                matched_intent=intent  
    
    # The fallback intent is selected by default
        key='fallback' 
        if matched_intent in responses:
        
        # If a keyword matches, the fallback intent is replaced by the matched intent as the key for the responses dictionary
            key = matched_intent 
    
    # The chatbot prints the response that matches the selected intent
        return responses[key]

                  

            
