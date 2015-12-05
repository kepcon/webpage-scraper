# Script:   webpage_get.py
# Desc:     Fetches data from a webpage.
# Author:   Rich Macf, edited by Connor Keppie
# Created:  Nov, 2014. edited Nov, 2015
#
import sys, urllib
        
def wget(url):
    ''' Try to retrieve a webpage via its url, and return its contents'''
    print '[*] wget()'
    # open file like url object from web, based on url
    webpage = urllib.urlopen(sys.argv[1])
    # get webpage contents
    page_contents = webpage.read()
    return page_contents

def main():
    # testing url argument
    #Uncomment line below to run this script from python shell
    #sys.argv.append('http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html')
    
    # Check args
    if len(sys.argv) != 2:
        print '[-] Usage: webpage_get URL'
        return

    # Get and analyse web page
    print wget(sys.argv[1])

if __name__ == '__main__':
	main()

