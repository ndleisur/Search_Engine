# project
Our search engine based on Killer Whales can be found at http://cgi.soic.indiana.edu/~ndleisur/
Crawler - crawl.py

Description:
Crawl reads in a user-inputted url, number, and folder to begin scraping. After initializing itself with not only the command line inputs, but also the rules, start_urls, num, directory, and finally creating the directory where all the html files will be kept. The start_url we just assigned with our user inputs begins the crawl in parse_url. Parse_url takes a spider and an http request response, and creates an instance of an item in our spider with it's full html body copied into item['html'] - which will later be transferred to a file and cleared - the url of the page the spider is currently crawling, and then extracts all the links from the page and assigns a list version of all the urls to the item to then go on to be processed, but not before we decrease the check to see if self.num is at zero, as to keep track of how many pages we have successfully crawled and know when our spider should stop. From there we head over to pipelines.py to process the information before we make any further decisions on whether or not to keep it. The class DuplicatesPipline does two major things: it gets rid of any of our spider items that are already in existence (and then increases the num by one, so that we can make sure we're keeping the number of pages we have successfully crawled and logged true) and then if it is not a duplicate, this pipeline creates an html file that is a copy of the item['html'], then clears out the item['html'] just to save a little space, adds the filename along with the page's url to the index.dat file, adds that filename to the item['filename'], and then finally returns the item. From there, we enter the FilterAndWritePipline, where we add our filename and url to a little dictionary called matches and append our item onto the list of all items within the spider while the spider is still open, and then upon the signalling that the spider is closed, this pipeline assembles the dictionary for our graph.dat file that reads in a dictionary, that has been converted into string format, of filenames of pages that have been crawled as keys and all of the filenames of the links that have been crawled off of their item['links'] list.

How to run:
~ cd killer_whale/spiders
~ python crawl.py *url* *number* *folder*

Indexer - index.py
Description:
Index takes a directory of html pages and a dat file of the names of the html files and the URLs at which the files can be found. It first parses the html of each page with beautiful soup, then takes out all stopwords and stems all remaining tokens. Index also creates bigrams for all stemmed tokens. At this point, Index outputs to two dat files, docs.dat and invindex.dat. In invindex, Index places a dictionary of all terms, both unigrams and bigrams, with the corresponding names of the pages on which they can be found and the number of occurances of the term in the page. In docs, Index places a dictionary of all of the names of the html files and their corresponding amount of tokens, webpage titles, and URLs.

How to run:
~ python index.py pages/ index.dat

Link Analysis - pagerank.py

Description:
Pagerank takes the graph.dat and outputs a dictionary to the pagerank.dat. This dictionary contains keys, whose values are their pagerank values. The pagerank values are based on a recursive algorithm. It starts with a damping factor, which serves to lessen the effects of the values on which pagerank is based for further iterations. One minus this is added to the product of the damping factor and the pagerank of all of the pages that link to the page divided by the number of all of the pages to which that page links. This allows a search engine to determine which pages are the most commonly visited.

How to run:
~ python pagerank.py *input file* *output file*
OR
~ python pagerank.py (will automatically select files if input and output files are not specified)

Web Interface - 

Retrieval and Ranking - retrieve.py, tfidf.py
Description:
Retrieve takes the inverted index and queries it for search terms. These search terms are rid of stopwords and stemmed. The or mode inclusively returns dictionary key values for each search term. The and mode exclusively returns dictionary key values for all search terms. The most mode returns dictionary key values if most (half or more) of the search terms appear in the documents. The printed values from the dictionary in docs.dat are the url and webpage title of each of the documents.

How to run:
~ python retrieve.py (search terms)

Description:
TF-IDF takes the invindex.dat and the tfidf.dat and outputs a dictionary to tfidf.dat. This dictionary has the same structure as invindex.dat, but instead of the number of times a term appears in a document, tfidf contains the tfidf score. The tfidf score is made of tf * idf. The tf is the term frequency, which is the number of times a term appears in a document diveded by the total number of terms in the document. The idf is the natural log of the total number of documents divided by the number of documents with the term in it. 

How to run:
~ python tfidf.py

Evaluation Experiments -

After running the original killer whale search on the term orca, both people were confused as to why the 10th option was British Columbia. The results didn't make sense to them and the search took about five seconds to get to the results page. Upon further investigation, we determined that the results were all from Wikipedia and they didn't understand why there would only be Wikipedia results and why the search engine results were only slightly aligned with the topic that they were searching about.

The next search they ran was on the term whale. Since it's a search engine called killer whale search, the fact that the results were not aligned to just killer whale results was very confused to them. Once again, the search results came up slowly.

Further Enhancements -

Extra Credit - 

