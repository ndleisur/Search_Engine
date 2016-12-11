#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import nltk
import urllib2
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stop = set(stopwords.words('english'))

def addPagesMost(hits, argv, terms, docs):
    invindex = eval(open('tfidf.dat', 'r').read())
    pagerank = eval(open('pagerank.dat', 'r').read())
    index = {}
    for term in argv:
        if term in invindex:
            for x in invindex[term]:
                if str(x) in index:
                    index[str(x)] += 1
                else:
                    index[str(x)] = 1
    for x in index:
        if index[x] >= terms / 2:
            hits = hits + [[docs[eval(x)[0]][1], docs[eval(x)[0]][2], eval(x)[1] * pagerank[eval(x)[0][6:]]]]
    return hits

def most(argv):
    argv = [term.lower() for term in argv if term not in stop]
    argv = [porter.stem(term) for term in argv]
    terms = len(argv)
    docs = eval(open('docs.dat', 'r').read())
    invindex = eval(open('tfidf.dat', 'r').read())
    work = False
    for term in argv:
        if term in invindex.keys():
            work = True
    #if work:
        #print 'Number of documents searched: ' + str(len(docs))

    # returns number of documents searched

        hits = []
        hits = addPagesMost(hits, argv, terms, docs)
        if len(hits) < 1:
            return None
        #print 'Number of hits: ' + str(len(hits))
        #print ' '
        #if len(hits) > 25:
            #print 'Showing the top 25 hits:'
        #elif len(hits) < 1:
            #print 'There are no search results available'
        #else:
            #print 'Showing the top ' + str(len(hits)) + ' hits:'
        i=25
        j=len(hits) - 1
        hits = sorted(hits, key=lambda hit: hit[2], reverse=True)[:10]
        #print "hits: " + str(hits)
        return hits
        while i > 0 and j > -1:
            print 'URL: ' + docs[hits[j][0]][2]
            print 'Title: ' + docs[hits[j][0]][1]
            print 'Tf-idf score: ' + str(hits[j][1])
            print 'Pagerank score: ' + str(hits[j][2])
            print 'Similarity score: ' + str(hits[j][1] * hits[j][2])
            print ' '
            j -= 1
            i -=1   
        else:
            return "No documents found"

if __name__ == '__main__':
    argv = sys.argv
    if len(sys.argv) > 1:
        argv = argv[1:]
        argv = [term.lower() for term in argv if term not in stop]
        argv = [porter.stem(term) for term in argv]
        most(argv)