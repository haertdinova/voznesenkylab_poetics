import nltk
import spacy
import re
import pymorphy2
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')

def n_words(text : str):
    words = word_tokenize(text, language='russian')
    num_words = len(words)
    return num_words

def n_sentences(text : str):
    sentences = sent_tokenize(text, language='russian')
    num_sentences = len(sentences)
    return num_sentences

def n_symbols(text : str):
    return len(text)

def n_syllables(text):
    syllables = re.findall(r'[аеиоуыэюяё]+', text, re.IGNORECASE)
    return len(syllables)

def n_letters(text):
    res = 0
    for sym in text:
        if sym.isalpha():
            res += 1
    return res

def lemmatized_no_pr_nouns(text):
    morph = pymorphy2.MorphAnalyzer()
    lemmatized_text = ''
    words = text.split()
    for word in words:
        normalized_word = morph.parse(word.lower())[0].normal_form
        if 'Name' not in morph.parse(word)[0].tag:
            lemmatized_text += normalized_word + ' '
    return lemmatized_text.strip()

def n_long_words(text):
    words = text.split()
    long_words = 0 #words with 3 or more syllables 
    for word in words:
        if n_syllables(word) >= 3:
            long_words += 1
    return long_words
