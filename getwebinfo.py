#Script: getwebinfo.py
#Desc: Runs all web gathering coursework scripts

#Created: Nov 2015

import sys, webpage_get, webpage_getfiles, webpage_getlinks, webpage_getuniqueinfo_crackhash

def getinfo(page, file_list):
    webpage_getlinks.print_links(page)
    webpage_getuniqueinfo_crackhash.print_email(page)
    webpage_getuniqueinfo_crackhash.print_phoneno(page)
    webpage_getuniqueinfo_crackhash.print_md5hash(page)
    webpage_getfiles.print_files(page, file_list)
    webpage_getfiles.check_file_hash(page, file_list)
    
    
def main():
    #testing url argument
    #Comment out line below to run this script from cmd line
    sys.argv.append('http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html')

    #Check args
    if len(sys.argv) != 2:
        print '[-] Usage: getwebinfo working-URL'
        return
    
    #Get webpage
    page = webpage_get.wget(sys.argv[1])
    #Create empty list
    file_list = []
    #Get info
    getinfo(page, file_list)

if __name__ == '__main__':
    main()
