#!/usr/bin/python
# -*- coding: utf-8 -*-
#Explaination of tf-idf from http://www.tfidf.com/

import sys
import math

def tf(freq, terms, docs):
    return float(freq) / float((docs[terms])[0])

def idf(length, docs):
    return float(math.log(float(len(docs.keys())) / float(len(length))))

def tf_idf(graph, docs):
    #initialize dictionary
    d = {}
    
    #Every key in the graph-dictionary gets a tf-idf value
    for key in graph.keys():
        #initialize d[key]
        d[key] = []
        #loop for all of the documents in which the term appears
        for x in graph[key]:
            #give new values for the tf-idf index with the pages the terms appear on and their tf_idf score
            d[key] = d[key] + [[x[0], tf(x[1],x[0],docs)*idf(graph[key], docs)]]
        
    #return dictionary to be printed in tfidf.dat
    return d
    
def main(argv):
    #open invindex.dat as filename1
    filename1 = eval(open('invindex.dat', 'r').read())
    #open tfidf.dat in preparation to save new dictionary to it
    filename2 = open('tfidf.dat', 'w')
    #open docs.dat as filename1
    filename3 = eval(open('docs.dat', 'r').read())
    
    #call tf_idf to write dictionary to tfidf.dat file
    filename2.write(str(tf_idf(filename1, filename3)))
    
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print 'error'
    else:
        main(sys.argv[1:])