import string

STOPWORDS = ["the","a","an","and","or","to","of","in","on","for","with","is","are","was","were","be","been","being","as","at","by","from"]

def text_cleaning(text):
    filtered_tokens=[]
    if text:
        translator = str.maketrans('','',string.punctuation)
        text = text.lower()
        text = text.translate(translator)
        text = " ".join(text.split())
        tokens = text.split()
        for token in tokens:
            if token not in STOPWORDS:
                filtered_tokens.append(token)
        return text, filtered_tokens


        

        