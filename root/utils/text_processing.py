import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def download_nltk_data():
    try:
        nltk.data.find('punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('wordnet')
    except LookupError:
        nltk.download('wordnet', quiet=True)
    
    try:
        nltk.data.find('stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)

download_nltk_data()

nlp = spacy.load("en_core_web_sm")
stopword_list = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    tokens_without_stopwords = [word for word in tokens if word.lower() not in stopword_list]
    text_without_stopwords = nlp(' '.join(tokens_without_stopwords))
    lemmatized_tokens = [token.lemma_ for token in text_without_stopwords]
    cleaned_data = [re.sub(r'[#*]', '', token) for token in lemmatized_tokens]
    cleaned_data = [re.sub(r'[-]{2,}', '', token) for token in cleaned_data]
    cleaned_data = [token for token in cleaned_data if token.strip()]
    cleaned_data = ' '.join(cleaned_data)

    return cleaned_data