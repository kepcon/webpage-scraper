#Script: webpage_getuniqueinfo_crackhash.py
#Desc: Basic web site info gathering and analysis script
#      From a URL gets page content, parsing md5hash hex numbers, email addresses and phone numbers
#      Produces formatted list of matched info
#      Cracks hash passwords using dictionary of common passwords
#Author Rich Macf, edited by Connor Keppie
#Created Nov, 2013 edited Nov 2015

import sys, re, hashlib
import webpage_get

def print_email(page):
    ''' finds and prints all email addresses in webpage '''
    #regex to find all emails
    emails = re.findall('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+', page)
    #sort then print emails
    emails.sort()
    print '[+]', str(len(emails)), 'Email addresses Found:'
    for email in emails:
        print email
        
def print_phoneno(page):
    ''' finds and prints all phone numbers in webpage  '''
    #regex to find all phone numbers in UK format
    phonenos = re.findall('\+44\(0\)\d+\s?\d+\s?\d+', page)
    #sort then print phone numbers
    phonenos.sort()
    print '[+]', str(len(phonenos)), 'Phone numbers Found:'
    for phoneno in phonenos:
        print phoneno

def print_md5hash(page):
    ''' find all hashes in webpage and compares against dictionary of password hashes to crack them'''
    #regex to find all md5hashes
    md5hashes = re.findall('([a-fA-F\d]{32})', page)
    #Dictionary of common passwords
    dic = ['123','1234','12345','123456','1234567','12345678','password', 'qwerty','abc','abcd','abc123','111111','monkey','arsenal','letmein','trustno1','dragon','baseball','superman','iloveyou','starwars','montypython','cheese','123123','football','password','batman']
    #sort then print hashes
    md5hashes.sort()
    print '[+]', str(len(md5hashes)), 'Hashes Found:'
    for  md5hash in md5hashes:
        print md5hash
        #Checks if password hash matches any of those in dictionary then prints
        #3rd hash ('joshua') doesn't match to any in dictionary
        for password_dic in dic:
            hashpasswd_dic = hashlib.md5(password_dic)
            if hashpasswd_dic.hexdigest() == md5hash:
                print 'Cracked password^: ', password_dic
                
    print 'No match found for hash^:'        

def main():
    #testing url argument
    #Uncomment line below to run this script from python shell    
    #sys.argv.append('http://www.soc.napier.ac.uk/~cs342/CSN08115/cw_webpage/index.html')

    #Check args
    if len(sys.argv) != 2:
        print '[-] Usage: webpage_getuniqueinfo_crackhash working-URL'
        return
    #Get webpage
    page = webpage_get.wget(sys.argv[1])
    #Get links
    print_email(page)
    print_phoneno(page)
    print_md5hash(page)
    

if __name__ == '__main__':
    main()
