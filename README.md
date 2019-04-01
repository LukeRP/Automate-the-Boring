# Automate-the-Boring
My implementations of the chapter projects from Automate the Boring Stuff with Python.

## Chapter 7 Projects:


  1.  Name: **"Phone Number and Email Address Extractor"**  
  
      * Finds phone numbers and email addresses on the clipboard.  
  
      * If the clipboard contains a web address, and only a web address, then instead of reading
      emails and phone numbers from the clipboard, it will instead scrape the webpage looking for 
      either email addresses or phone numbers.  

      * File: ```"pyperclip-regex.py"```  
      
      * My Tweaks: adding an automatic web-scraping method, and encapsulating all of the functionality inside of a class. 
      
  
## Chapter 8 Projects:  

  
  1.  Name: **"Generating Random Quiz Files"**  
  
      * Creates random quiz questions and their respective answer keys.

      * This program will take the number of students in a class (or the desired number of individual tests) and make a unique multiple-choice quiz for each. The current implementation is for testing state capitals, but can be generalized for any "zero sum" quiz, such as vocabulary for a unit or any other test where the answer choices besides the correct one for a given question don't matter (e.g. this would be a poor way to generate random math quizzes, unless one simply wanted to switch up the /order/ of questions and their answers and not randomize the selection of wrong answer choices as well.)
  
      * File: ```"quiz_gen.py"```  
      
      * My Tweaks: checking for the maximum number of unique quizzes, ensuring the quizzes are actually random, and replacing the string formatting %'s with .format().  
      
      
  2.  Name: **"Searching Directories using Regex"**  
  
      * This program will 1) take a string, 2) open every .txt file in a directory, 3) perform a regex search to find all (if any) instances of that string in the files, and 4) print matches to the screen (terminal).
  
      * File: ```"regex_search.py"```  
      
      
  3.  Name: **"Multiclipboard"**
  
      * Saves and loads pieces of text to the clipboard, tied to keywords for easy recall.

      * E.g.:   
        * ```./mcb.py save <keyword>```     - saves clipboard contents to keyword
        * ```./mcb.py <keyword>```         - loads associated keyword's contents to clipboard
        * ```./mcb.py list```               - lists all currently saved keywords
        * ```./mcb.py delete <keyword>```   - delete keyword from list
        * ```./mcb.py clear```              - delete all keywords from shelf
  
      * File: ```"mcb.py"```  
      
      * My Tweaks: added a "Delete" functionality which also checks if the key exists.
      
      
## Chapter 9 Projects:

  1.  Name: **"Zip-A-Folder"**  
      
      * Copies an entire folder and its contents into a .zip file, the name of which increments with each backup, e.g. "zipped_1" > "zipped_2".
  
      * File: ```"zipper.py"```  
