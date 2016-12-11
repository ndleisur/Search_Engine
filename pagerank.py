#!/usr/bin/python
# -*- coding: utf-8 -*-
#Explaination of pagerank from http://pr.efactory.de/e-pagerank-algorithm.shtml

from __future__ import division
import sys
import copy

def C(graph,key):
    #returns number of outbound links on page key
    result = len(graph[key])
    return result

def PR(graph, key, result1, result2):
    #Result starts at 1 - D_factor = 0.5
    #Damping factor set to .8
    D_factor = .8
    #When the difference gets small, return result
    if abs(copy.deepcopy(result1) - copy.deepcopy(result2)) < 0.0000000000000000001:
        return result2
    else:
        #Damping factor plus pagerank of pages that link to this one divided by number of outbound links on that page
        #x is a key in dictionary graph
        for x in graph.keys():
            #if key from pagerank loop in this key's value list graph[x]
            if key in graph[x]:
                result1 = copy.deepcopy(result2)
                result2 = (1 - D_factor) + (D_factor * (PR(graph,x, result1, result2)/C(graph,x)))
                return result2

def pagerank(graph):
    #initialize dictionary
    d = {}
    
    #solve dangling node problem
    for key in graph.keys():
        if len(graph[key]) < 1:
            graph[key] = graph.keys()
    
    #Every key in the graph-dictionary gets a pagerank value
    for key in graph.keys():
        d[key] = PR(graph, key, 0, .8)
        
    #return dictionary to be printed into pagerank.dat
    return d
    
def main(argv):
    #open graph.dat as filename1
    file1 = argv[0]
    filename1 = eval(open(file1, 'r').read())
    
    #open pagerank.dat in preparation to save new dictionary to it
    file2 = argv[1]
    filename2 = open(file2, 'w')
    
    #call pagerank to write dictionary to pagerank.dat file
    dic = str(pagerank(filename1))
    print dic
    filename2.write(dic)
    
    #close files
    filename2.close()
    #filename1.close()
    
if __name__ == '__main__':
    #type graph file and pagerank file into the command line, else run on predetermined files
    if len(sys.argv) == 1:
        #this means you can run this function on the command line without variables
        sys.argv.append('graph.dat')
        sys.argv.append('pagerank.dat')
        print "running on predermined files"
    if len(sys.argv) != 3:
        print 'error'
    else:
        main(sys.argv[1:])