# Automate-the-Boring
My implementations of the chapter projects from Automate the Boring Stuff with Python.

Chapter 7 Projects:

  1.  Name: "Phone Number and Email Address Extractor"  
  
      pyperclip-regex.py - Finds phone numbers and email addresses on the clipboard.  
  
      If the clipboard contains a web address, and only a web address, then instead of reading
      emails and phone numbers from the clipboard, it will instead scrape the webpage looking for 
      either email addresses or phone numbers.  

      File: pyperclip-regex.py  
      
      My Tweaks: adding an automatic web-scraping method, and encapsulating all of the functionality inside of a class. 
  
Chapter 8 Projects:  
  
  1.  Name: "Generating Random Quiz Files"  
      File: quiz_gen.py  
      My Tweaks: checking for the maximum number of unique quizzes, ensuring the quizzes are actually random, and replacing the string formatting %'s with .format().  
      
  2.  Name: "Searching Directories by Regex"  
      File: regex_search.py  
      
  3.  Name: "Multiclipboard"
      File: "mcb.py"  
      My Tweaks: added a "Delete" functionality which also checks if the key exists.
      
Chapter 9 Projects:

  1.  Name: "Zip-A-Folder"  
      File: "zipper.py"  
