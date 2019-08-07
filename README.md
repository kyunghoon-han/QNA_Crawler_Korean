# QNA_Crawler_Korean
This small code accesses to Naver's Q&A system called 지식in (Jisik-in). 

## How to run the code?
One simply needs to run the following on terminal to run the code.
```
python3 main.py
```
The crawler first accesses the page 1 of the web-page, then successively move on to the new pages.
JSON format files of dictionaries containing the following information is then created for each page of Q&As:
* Question Title
* Question Details
* Number of Responders
* Level of Responder 
* Answer
The last two entries are grouped under a category of "Answer Contents"

## A couple of parameters a user may like to change
The line 10 of the main.py file contains the following:
```
num_page = 1
```
one can change this number to any integral value greater than or equal to 1 to start running the code from a Q&A page other than the 1st page.
The next parameter then says:
```
max_page = num_page + 10000
```
one can change the number after the + sign to adjust the amount of pages the crawler tries to access. 
