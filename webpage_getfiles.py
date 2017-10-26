#Script: webpage_getfiles.py
#Desc: Basic web site info gathering and analysis script
#      From a URL gets page content, parsing files out.
#      +Produces formatted list of matched files
#      +Downloads all files found in list
#      +Compares downloaded files with a set of bad hashes
#Created Nov, 2013 edited Nov 2015

import sys, re, urllib, os, hashlib
import webpage_get

def print_files(page, file_list):
    ''' find all files on a webpage, list and download them'''
    print '[*] print_files()'
    #regex to find .jpg,.gif,.bmp and docx files on the webpage
    files = re.findall('([\w-]+\.(?:jpg|gif|bmp|docx))', page)
    #sort + print files
    files.sort()
    print '[+]', str(len(files)), 'Files Found:'
    for  file1 in files:
        #Retrieves every file in list and downloads them
        downloadfile = sys.argv[1].replace("index.html", file1)
        print file1
        #SPECIFY DOWNLOAD PATH
        urllib.urlretrieve(downloadfile, "C:\\temp\\coursework\\" + file1)
        #Adds all downloaded files to list
        file_list.append("C:\\temp\\coursework\\" + file1)

def check_file_hash(page, file_list):
    ''' compares downloaded files against list of hashes, reports bad files'''
    bad_hash_dic = {'9d377b10ce778c4938b3c7e2c63a229a': 'contraband_file1.jpg',
                    '6bbaa34b19edd6c6fa06cccf29b33125': 'contraband_file2.jpg',
                    'e4e7c3451a35944ca8697f9f2ac037f1': 'contraband_file3.jpg',
                    '1d6d9c72e3476d336e657b50a77aee05': 'contraband_file4.gif'}
    
    #Opens and reads downloaded files
    try:
        for Lfiles in file_list:
            f = open(Lfiles, 'rb')
            filecontent = f.read()
            #Creates md5hash of downloaded files to compare to bad hashes
            bad_hash = hashlib.md5(filecontent)
            if bad_hash.hexdigest() in bad_hash_dic:
                print 'Bad file found: ' + Lfiles                
    except:
        print 'Exception: Files could not be read, cannot compare against bad hashes'

def main():
    #testing url argument
    #Uncomment line below to run this script from python shell
    #sys.argv.append('http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html')

    #Check args
    if len(sys.argv) != 2:
        print '[-] Usage: webpage_getfiles working-URL'
        return
    #Get webpage
    page = webpage_get.wget(sys.argv[1])
    #Create empty list
    file_list = []
    #Get links
    #Passes file_list into both functions
    print_files(page, file_list)
    check_file_hash(page, file_list)

if __name__ == '__main__':
    main()
