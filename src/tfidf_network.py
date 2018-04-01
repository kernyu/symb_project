import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
# nltk.download('punkt')
# tokenizers/punkt/english.pickle
from nltk.tokenize import RegexpTokenizer
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize
tokenizer = RegexpTokenizer(r'\w+')

corpus_root = 'abstract_50_90'
corpus = PlaintextCorpusReader(corpus_root,fileids='[0-9]+')

stop_words = stopwords.words() + list(punctuation) + ['None','Non']

def tokenize(text):
    words = word_tokenize(text)
    words = [w.lower() for w in words]
    return [w for w in words if w not in stop_words and not w.isdigit()]

vocabulary = set()
for file_id in corpus.fileids():
    words = tokenize(corpus.raw(file_id))
    vocabulary.update(words)

vocabulary = list(vocabulary)
# word_index = {w: idx for idx, w in enumerate(vocabulary)}

# VOCABULARY_SIZE = len(vocabulary)
# DOCUMENTS_COUNT = len(corpus.fileids())

# word_idf = defaultdict(lambda: 0)
# for file_id in corpus.fileids():
# words = set(tokenize(corpus.raw(file_id)))
# for word in words:
# word_idf[word] += 1
# for word in vocabulary:
# word_idf[word] = math.log(DOCUMENTS_COUNT / float(1 + word_idf[word]))

# print(word_idf['mrsa'])
# print(word_idf['antibiotic'])

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words=stop_words, tokenizer=tokenize, vocabulary=vocabulary)
# Fit the TfIdf model
tfidf_mat = tfidf.fit_transform([corpus.raw(file_id) for file_id in corpus.fileids()])
np.savetxt('tfidf_50_90',tfidf_mat,delimiter=',',fmt='%1.4e')
