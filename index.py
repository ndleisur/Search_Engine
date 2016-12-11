#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import nltk
import urllib2
from nltk import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
import copy
from copy import deepcopy
stop = set(stopwords.words('english'))
import hashlib
from collections import Counter


def main(argv):

    # Initialize the directory as dire

    dire = argv[0]

    # Initialize the .dat file as index

    index = open(dire + argv[1]).readlines()

    index_len = len(index)

    i = 0
    tokens = []
    file3 = argv[3]
    filename3 = open(file3, 'w')
    file2 = argv[2]
    filename2 = open(file2, 'w')
    h={}
    docs={}
    while i < index_len:

        # file1 = open(dire + index[i].split()[0]).read()
        
        soup = BeautifulSoup(open(dire + index[i].split()[0]),
                             'html.parser')
        title = soup.title.string
        for part in soup.findAll(['script', 'style']):
            part.extract()
        doc_title = soup.title
        raw = soup.get_text()
        tokens = word_tokenize(raw)
        tokens = [word.lower() for word in tokens
                  if word not in string.punctuation if '.jpg'
                  not in word if not word.isdigit()]

        # print tokens
        # token_count=0
        tokens = [word.lower() for word in tokens if word not in stop]
        tokens = [porter.stem(token) for token in tokens]
        tokens = tokens + list(nltk.bigrams(tokens))

        # print tokens

        token_count = len(tokens)

        # curr_url =
        
        freqs = Counter(tokens)
        freqs2=copy.deepcopy(freqs)
        #How often a term appears in a document
        #print freqs
        for word in tokens:
            if word in h and freqs2[word] > 1:
                freqs2[word] = freqs2[word] - 1
            elif word in h:
                h[word]= h[word] + [[dire + index[i].split()[0], freqs[word]]]
            else:
                h[word] = [[dire + index[i].split()[0], freqs[word]]]

        docs[dire + (index[i].split()[0])] = [str(token_count),title,str(index[i].split()[1])]
        #adds to hash for docs.dat 
        i += 1
    filename3.write(str(docs))
    filename2.write(str(h))
    filename3.close()
    filename2.close()


    # Print the contents of invindex.dat

    # print nltk.tokenize(fil[0])
    # for x in index:
        # print dire + x.split()[0]
        # print open(dire + x.split()[0]).readlines()

if __name__ == '__main__':
    sys.argv.append('invindex.dat')
    sys.argv.append('docs.dat')
    if len(sys.argv) != 5:
        print 'error'
    else:
        main(sys.argv[1:])
