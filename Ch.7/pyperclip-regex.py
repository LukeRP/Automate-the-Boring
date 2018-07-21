#! /usr/bin/env python3
'''
Project from Ch. 7 of Automate the Boring Stuff with Python
  
pyperclip-regex.py - Finds phone numbers and email addresses on the clipboard.
  
If the clipboard contains a web address, and only a web address, then instead of reading
emails and phone numbers from the clipboard, it will instead scrape the webpage looking for 
either email addresses or phone numbers.  
  
In order to make this run from the command line without too much hassle, this has
been mostly automated. 
  
However, in the event that I wanted to port this functionality to another script,
and moreover just to learn and keep things tidy, I've implemented it as a class.
'''

import pyperclip as clip
import regex as re
import requests
import bs4
from bs4 import BeautifulSoup


class NumberMail(object):
    
    '''
    NumberMail instances contain all of the (pre-cached) regex compilations needed
    to find phone numbers, emails, and urls, as well as the proper headers for 
    a Request object. 
    
    Its methods are fairly self-explanatory:
    get_numbers() will match 10 digit phone numbers;
    get_emails() will match almost any valid email address;
    rip_from_site() creates Request and BeautifulSoup objects and 
        asks the user if they want to rip either numbers of emails 
        from the resulting text;
    rip_from_clip() does the same for whatsoever is on the clipboard,
        and will rip_from_site() automatically if it detects a URL.
    '''
    
    headers = {'User-Agent':   'Mozilla/5.0 \
                                (Macintosh; Intel Mac OS X 10_10_1) \
                                AppleWebKit/537.36 \
                                (KHTML, like Gecko) \
                                Chrome/39.0.2171.95 \
                                Safari/537.36'}
    
    phoneRegex = re.compile(r'''(
                    (\d{3}|\(\d{3}\))?              # area code - w/wo parentheses
                    (\s|-|\.)?                      # separator - space or dash
                    (\d{3})                         # central office code
                    (\s|-|\.)                       # separator - space or dash
                    (\d{4})                         # line number
                    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
                    )''', re.VERBOSE)
    
    emailRegex = re.compile(r'''(
                    (.*[\w]+[._%+-]*)               # username
                    @                               # "at" symbol
                    ([a-zA-Z0-9.-]+)                # domain name
                    (\.[a-zA-Z]{2,5})               # "dot" whatever
                    )''', re.VERBOSE)

    # N.B. urlRegex does not include any hashes at the end of a URL, but should be fine for determining if it's a URL at all.
    urlRegex = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    def rip_from_site(self, site):
        
        r = requests.get(site, headers=self.headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        text = soup.text
        
        while True:
            
            answer = input('Do you want "1" Phone Numbers or "2" Emails? (Please enter a number)')
        
            if int(answer) == 1:
                return self.get_numbers(text)
            elif int(answer) == 2:
                return self.get_emails(text)
            else:
                print('Not a valid choice: please enter a "1" or a "2"')
        
    def get_numbers(self, text):
        
        matches = []
        
        for groups in self.phoneRegex.findall(text):
            
            phoneNum = '-'.join([groups[1], groups[3], groups[5]])
            
            if groups[8] != '':
                phoneNum += ' ext. ' + groups[8]
                
            matches.append(phoneNum)
        
        if len(matches) > 0:
            clip.copy('\n'.join(matches))
            print('Numbers copied to clipboard:')
            print('\n'.join(matches))
        else:
            print('No numbers found.')
            
        return matches
        
    def get_emails(self, text):
        
        matches = []
        
        for groups in self.emailRegex.findall(text):
            matches.append(groups[0])
          
        if len(matches) > 0:
            clip.copy('\n'.join(matches))
            print('Emails copied to clipboard:')
            print('\n'.join(matches))
        else:
            print('No emails found.')
            
        return matches 

    def rip_from_clip(self):   
        
        text = str(clip.paste())
        
        if self.urlRegex.findall(text) and '\n' not in text:
            
            self.rip_from_site(text)
        
        else:
            
            while True:
            
                answer = input('Do you want "1" Phone Numbers or "2" Emails? (Please enter a number)')
            
                if int(answer) == 1:
                    return self.get_numbers(text)
                elif int(answer) == 2:
                    return self.get_emails(text)
                else:
                    print('Not a valid choice: please enter a "1" or a "2"')
            
def test_it_out():
    
    site = 'https://www.verizonwireless.com/support/contact-us/#PhoneNumbers'
    
    tester = NumberMail()
    
    tester.rip_from_site(site)
    
if __name__ == "__main__":
    
    run_script = NumberMail()
    run_script.rip_from_clip()
    
