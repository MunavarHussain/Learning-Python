# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:06:14 2019

@author: AKMH
"""

import re

#print(r'Hi\tTab') #r denotes raw string

txt = '''Start
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Metacharacters :
    . ^ $ * + ? { } [ ] \ | ( )
    
google.com

123-456-2344
123.345.5674
123*345*5674
       
Mr. Hussain
Mr Ashraf
Ms Davis
Mrs. Robi
Mr. T 

cat
mat
sat
bat

end'''


#pattern = re.compile(r'\bHa\b')
#pattern = re.compile(r'^abc') 
#pattern = re.compile(r'^Start')
#pattern = re.compile(r'^St') 
#pattern = re.compile(r'end$')
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern = re.compile(r'\d{3}[.-]\d{3}[-.]\d{4}')
#pattern = re.compile(r'\d{3}[.-*]\d{3}[-.*]\d{4}') error
#pattern = re.compile(r'\d{3}[.*-]\d{3}[-.*]\d{4}')

#pattern = re.compile(r'[1-5]')
#pattern = re.compile(r'[^a-zA-Z]')
#pattern = re.compile(r'[^b]at')
#pattern = re.compile(r'\d{3}.\d{3}.\d{3,4}')


#pattern = re.compile(r'[89]00[.-]\d{3}[.-]\d{4}')
#with open('data.txt','r') as f:
#    contents = f.read()
#    matches = pattern.finditer(contents)
#
#    for match in matches:
#        print(match)
  

#pattern = re.compile(r'M[rs]+\.?\s[\w]+')
#pattern = re.compile(r'M(r|rs|s)\.?\s[A-Z]\w+')
#pattern = re.compile(r'M(r|rs|s)\.?\s[A-Z]\w?')
#pattern = re.compile(r'M(r|rs|s)\.?\s[A-Z]\w*')
#pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')
#matches = pattern.finditer(txt)

emails = """
munavarHussain@gmail.com
munvar.hussain@univ.edu
munavar-123-hussain@my-cmpy.net

"""

#pattern = re.compile(r'[\w]*@gmail.com')
#pattern = re.compile(r'[a-zA-Z]+\.?[\w]*@[\w]*.(com|edu)')
#pattern = re.compile(r'([a-zA-Z]+)\.?([\w]*@[\w])*.(com|edu)')
#pattern = re.compile(r'([a-zA-Z]+)\.?([\w]*)(@[\w]*).(com|edu)')
#pattern = re.compile(r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.(com|edu|net)')
#pattern = re.compile(r'([\w.-]+)@([\w-]+\.(com|edu|net))')
#pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+')
#matches = pattern.finditer(emails)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

#pattern = re.compile(r'http[s]?://(www.)?([a-z]+.[a-z]+)')
#pattern = re.compile(r'https?://(www\.)?([\w]+)(\.[\w]+)') #    print(match.group(2)+match.group(3))
#pattern = re.compile(r'https?://(www\.)?(([\w]+)(\.[\w]+))') #print(match.group(2))
#matches = pattern.finditer(urls)
#for match in matches:
#    print(match)
#    print(match.span())
#    print(match.group(2)+match.group(3))
#    print(match.group(2)) 


#pattern = re.compile(r'https?://(www\.)?([\w]+)(\.[\w]+)')
#matches = pattern.finditer(urls)
#sub_urls = pattern.sub(r'\2\3',urls)
##      In urls Whereever pattern found, substitute by group 2&3 
#print(sub_urls)


#pattern = re.compile(r'\d{3}[.*-]\d{3}[-.*]\d{4}')
#matches = pattern.findall(txt) #lists the matches
#for match in matches:
#    print(match)


#pattern = re.compile(r'Start')
#matches = pattern.match(txt)
#print(matches)

pattern = re.compile(r'Ha')
pattern = re.compile(r'start',re.IGNORECASE) #or re.I (shorthand)
matches = pattern.search(txt)
print(matches)
