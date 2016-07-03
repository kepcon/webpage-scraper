# webpage-scraper
Python web scraping/info gathering utility created for Applications Development module.

Enter link into getwebinfo.py script then run to call all other scripts.
Each script can be run individually by uncommenting the specified line in that script.

###webpage_get : 
Retrieves html structure of website via URL.

###webpage_getfiles : 
Retrieves page content via URL, parsing out files. Downloads all files and produces formatted list of   matched files(download path must be specified in script). Compares downloaded files with a set of bad hashes.

###webpage_getlinks : 
Parses links out of page content and produces formatted list of matched links. 

###webpage_getuniqueinfo_crackhash : 
Retrieves page content, parses md5hash hex numbers, email addresses and phone numbers then produces a formatted list of matched information. Cracks hash passwords using dictionary of common passwords.
