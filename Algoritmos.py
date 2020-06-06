
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

def __LevenshteinAlgorit(caract1, caract2):
    '''caract 1 é o caracter que voce vai pesquisar, o caracter 2 é o da base de dados '''
    if caract1 == '':
        return len(caract2)
    elif caract2 == '':
        return len(caract1)
    else:
        soma = 0 if caract1[0] == caract2[0] else 1
        soma += __LevenshteinAlgorit(caract1[1:], caract2[1:])
        return soma
def after_token(caract1, caract2):

        return round(__LevenshteinAlgorit(caract1, caract2)/max(len(caract1), len(caract2)), 2)

def valueLevensh(caract1, caract2):
    try:    
        cont = 0
        stemmer = nltk.stem.RSLPStemmer()
        stopwords = set(nltk.corpus.stopwords.words('portuguese'))
        key = word_tokenize(caract1)
        key2 = [kw for kw in key if not kw in stopwords and kw.isalnum()]
        size = len(key2)
        for ikey in key2:
            ikey = stemmer.stem(ikey)
            ikey, caract2 = ikey.lower(), caract2.lower()
            word_tokens = word_tokenize(caract2)
            filtered_sentence = [w for w in word_tokens if not w in stopwords and w.isalnum()]         
            for words in filtered_sentence:
                words = stemmer.stem(words)
                if 0.3 > after_token(ikey, words):
                    cont += 1
                    break
        if cont >= size:
            return True
        else:
            return False
    except:
        return
def show_pretty(words):
    new = ''
    for i in words:
        if not(i == '[' or i == ']' or i =='"'):
            new = new + i 
    return new
