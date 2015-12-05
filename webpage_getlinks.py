#Script: webpage_getlinks.py
#Desc: Basic web site info gathering and analysis script
#      From a URL gets page content, parsing links out.
#      Produces formatted list of matched links
#Author: Rich Macf, edited by Connor Keppie
#Created: Nov, 2013 edited Nov 2015

import sys, re
import webpage_get

def print_links(page):
    ''' find all hyperlinks on a webpage passed in as input and print'''
    print '[*] print_links()'
    #regex to match on hyperlinks
    links = re.findall(r'(?:http[s]?://|www.)[^"\' ]+', page)
    #sort + print links
    links.sort()
    print '[+]', str(len(links)), 'Hyperlinks Found:'
    for  link in links:
        print link

def main():
    #testing url argument
    #Uncomment line below to run this script from python shell
    sys.argv.append('http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html')

    #Check args
    if len(sys.argv) != 2:
        print '[-] Usage: webpage_getlinks working-URL'
        return
    #Get webpage
    page = webpage_get.wget(sys.argv[1])
    #Get links
    print_links(page)

if __name__ == '__main__':
    main()
