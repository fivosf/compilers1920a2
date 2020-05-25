import re

#.................Building expressions........................

#remove title tag expression
removeTitle = re.compile('<title>(.*?)</title>')

#remove comments expression
removeComments = re.compile('<!--.*?-->',re.DOTALL)

#remove style and script tag and all its contents expression
removeCode = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL)

#remove a tags
removeLinks = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)

#remove special chars
removeSpecial = re.compile(r'&(amp|gt|lt|nbsp);')

#remove unneccecary white spaces
removeWhitespaces = re.compile(r'\s+') 

#remove all other tags
removeAllTags = re.compile(r'<.*?>',re.DOTALL)


def replace(m):
    if (m.group(0)=='&amp;'):
        return '&'
    elif (m.group(0)=='&gt;'):
        return '>'
    elif (m.group(0)=='&lt;'):
        return '<'
    else:
        return ' '

#............opening testpage.txt for reading................
with open('testpage.txt','r') as fp:

    text = fp.read() 

    # Striping the title tags
    title = removeTitle.search(text)

    #printing the title... I thing that the same can be done with removing all the tags so in the 
    #final text this gives two titles.
    print(title.group(1))	

    #Removing all the comments
    text = removeComments.sub(' ',text)

    #Removing code (styles and scripts)
    text = removeCode.sub(' ',text)

    #Replacing special chars width the help of the replace function
    text = removeSpecial.sub(replace,text)

    urls = ""

    #Writing all urls in a new string
    for link in removeLinks.finditer(text):
        urls = urls + '{} {}'.format(link.group(1),link.group(2))

    #Removing all tags from urls string... I did this to remove images and alt tags
    # I wanted to display only links and text of the links
    urls = removeAllTags.sub(' ',urls)  

    #Removing all tags
    text = removeAllTags.sub(' ',text)  
        

    #Replacing whitespaces with a single white space
    text = removeWhitespaces.sub(' ',text)      

    #Printing the final text
    print(text)

    #Printing urls
    print(urls)
