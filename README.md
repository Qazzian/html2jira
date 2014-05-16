# html2jira


html2jira is a Python script that converts a page of HTML into the wiki format used by Atlassian's Jira and Confluance applications.

Usage: `html2jira.py [(filename|url) [encoding]]`

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      --ignore-links        don't include any formatting for links
      --ignore-images       don't include any formatting for images
      -g, --google-doc      convert an html-exported Google Document
      -d, --dash-unordered-list
                            use a dash rather than a star for unordered list items
      -b BODY_WIDTH, --body-width=BODY_WIDTH
                            number of characters per output line, 0 for no wrap
      -i LIST_INDENT, --google-list-indent=LIST_INDENT
                            number of pixels Google indents nested lists
      -s, --hide-strikethrough
                            hide strike-through text. only relevent when -g is
                            specified as well

Or you can use it from within Python:

    import html2jira
    print html2jira.html2jira("<p>Hello, world.</p>")

Or with some configuration options:

    import html2jira
    h = html2jira.HTML2Text()
    h.ignore_links = True
    print h.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>!")

_Originally written by Aaron Swartz. This code is distributed under the GPLv3._


## How to install

clone this repository, open your terminal, navigate to the root directory and run
    
    python setup.py install

You may need admin privaliges 


## How to run unit tests

    python test/test_html2text.py -v
