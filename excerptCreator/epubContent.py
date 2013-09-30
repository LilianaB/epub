# -*- coding: ISO-8859-1 -*-
from django.utils import text, html
from BeautifulSoup import BeautifulSoup, Tag
import re
import sys

class epubContent:
    
    def __init__(self,content):
        self.content = content
    
    def addCover(self):
        self.content = self.content.replace("<body>", "<body><div align='center'>"+\
            "<img src='images/cover.jpg'"+\
            "id='icontxt' class='icon'/></div>",1)
        
    def addDoctype(self):
        self.content = self.content.replace("<head>", '<head><title>Liebe, Sex und andere Katastrophen</title>',1)
        self.content = self.content.replace("<html>", '<html xmlns="http://www.w3.org/1999/xhtml">',1)
        self.content = self.content.replace("&nbsp", "&#160")
        self.content = self.content.replace("&ndash", "&#8211")
        self.content = '<?xml version="1.0" encoding="utf-8"?> \n'+\
        self.content
        self.content = unicode(self.removeATags())
        
    def countWords(self):
        return len(self.splitIntoWords())

    def truncate(self, numberOfWords):
        return text.truncate_html_words(self.content, numberOfWords)
            
    def addFooter(self,footer): 
        contentWithoutClosingTags = self.content.rsplit('<', 2)[0]
        self.content = contentWithoutClosingTags + footer
    
    def splitIntoWords(self):
        return self.content.split();

    def prepareFooter(self, footer):
       return "<br><br><br> <hr width=60%/><b>"+footer.encode('utf-8')+\
       "</b></body></html>"
       
    def addUtf8Encoding(self):
        self.content = self.content.encode('UTF-8')
        return self
        
    def getSizeOfTheExcerpt(self, percentage):
        return int(self.countWords()*float(percentage))
    
    def generateExcerptContent(self,percentage):
        try:
            size = self.getSizeOfTheExcerpt(percentage)
            return self.truncate(size)
        except Exception as e:
            print e
            print "Problem truncating html content"
            
    def removeATags(self):
        soup = BeautifulSoup(self.content)
        aTags = soup.findAll('a')
        [aTag.replaceWith(aTag.text) for aTag in aTags]
        #for aTag in aTags:
         #   bTag = Tag(soup, 'b')
          #  bTag.insert(0, aTag.text)
           # aTag.replaceWith(aTag.text)'''
            
        #[aTag.extract() for aTag in aTags]
        return soup
        
    def replaceATags(self):
        soup = BeautifulSoup(self.content)
        btag = Tag(soup, 'b')
        soup.a.replaceWith(btag)
        return soup
        
    def getHref(self):
        soup = BeautifulSoup(self.content)
        for tag in soup.findAll('a', href=True):
            tag['href'] = re.sub(r'^#.*', r'', tag['href'])
        return soup
        
        
    def __getImageTags(self):
        soup = BeautifulSoup(self.content)
        return soup.findAll('img')
        
    def __getImageSrcFromTag(self, imageTags):
        imageNames = []
        for tag in imageTags:
            imageNames.append(str(self.__removePathFromImageTag(tag.get('src'))))
        return imageNames
        
    def __removePathFromImageTag(self,imageTag):
        split = str(imageTag).split('/',1)
        return split[1] if len(split)==2 else split[0]
        
    def getImages(self):
        return self.__getImageSrcFromTag(self.__getImageTags())
