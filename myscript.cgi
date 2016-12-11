#!/usr/bin/python
import cgi
from retrieve import most
import sys
import string
import nltk
import urllib2
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# Base of the html content
CONTENT = """
<html>
<head>
<title>Interactive Page</title>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
<container>
<div class="col-xs-offset-2 col-xs-6">
<div style="position:fixed;background-color:white;width:700px;">
    <a href="index.html" style="color:black;"><h1>Find Killer Whales</h1></a>
    <form method=POST action="myscript.cgi">
        <P><B>Your latest query is "%s" </B>
    </form>
</div>
<br/><br/><br/><br/>
    <h2>Results</h2>
    %s
    <form method=POST action="myscript.cgi">
    <P><B>That was fun! Enter your next query below:</B>
        <P><input type=text name=query>
        <P><input type=submit>
    </form>
</div>
</container>
</body>
</html>
"""


def format_results(results):
    # join hyperlink tags with newlines
    return '\n'.join(
        '<a id="result" href="%s">%d. %s</a><br><p>Similarity Score: %s</p>' % (url[1], idx + 1, url[0], url[2])
        for idx, url in enumerate(results)
    )


def main():
    print "Content-Type: text/html\n\n"
    # parse form data
    form = cgi.FieldStorage()

    # get the query, if any, from the form
    if 'query' in form:
        query_str = cgi.escape(form['query'].value)
    else:
        query_str = '"empty query"'

    # TODO: process your query and get hit results
    # Result should be a list of url strings

    # format URL strings in results into hyperlinks
    results = most(query_str.split())
    if results is None or len(results) == 0:
        result_str = '<h3>Empty result: No Hit</h3>'
    else:
        result_str = format_results(results)

    # format your final html page
    print CONTENT % (query_str, result_str)


if __name__ == '__main__': main()
