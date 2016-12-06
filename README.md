#fetchproref

This command line tool will hit a pro reference site and download all tables as a CSV, then dump them all in folder at the current location. The folder name is the title of the url provided, slugified. The CSV name is derived from the ID to the HTML table.

This tool should play nicely with most Pro-Reference sites, except for [http://www.baseball-reference.com/](http://www.baseball-reference.com/), which has not been upgraded.

##Installing

Run this command in the terminal:

`sudo pip install fetchproref`

##Usage

Currently, there is only one way to use the tool, but it will work for all URLS.

`fetchproref fetch [URL]`

The URL can be any page in the Pro Reference universe that contains tables.