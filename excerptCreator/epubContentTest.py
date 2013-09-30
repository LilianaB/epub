# -*- coding: ISO-8859-1 -*-
#Extract new book
#zipfile.ZipFile(filepath).extractall(path=self.cache_path)
#Set permissions
#os.system("chmod 700 "+self.cache_path)

#Extract new book
#zipfile.ZipFile(filepath).extractall(path=self.cache_path)
#Set permissions
#os.system("chmod 700 "+self.cache_path)
from epubContent import *
import unittest
import os
from django.utils.encoding import smart_str

class epubConverterTests(unittest.TestCase):
    
    def setUp(self):
        content = "<html><head><meta http-equiv='Content-Type'"+ \
        "content='text/html;charset=utf-8' /></head><body>"+\
        "<h1>HTML Ipsum Presents </h1><p><strong>Pellentesque "+ \
        "habitant morbi tristique</strong> senectus et netus et malesuada"+ \
        "fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae," + \
        "ultricies eget, tempor sit amet, ante. Donec eu libero</body></html>"
        
        self.image = "<body><div align='center'>"+\
            "<img src='images/cover.jpg'"+\
            "id='icontxt' class='icon'/></div>"
        self.footer = "<div> this is the footer</div>"
        self.epubContent = epubContent(content)
        
    def testAddCover(self):
        self.epubContent.addCover()
        print self.epubContent.content
        self.assertTrue(self.image in self.epubContent.content)
        
    def testCountWords(self):
        splittedContent = self.epubContent.content.split()
        self.assertEqual(self.epubContent.countWords(), len(splittedContent))
        
    def testTruncate(self):
        expectedContent = "<html><head><meta http-equiv='Content-Type'"+ \
        "content='text/html;charset=utf-8' /></head><body>"+\
        "<h1>HTML Ipsum Presents </h1><p><strong>Pellentesque "+ \
        "habitant ...</strong></p></body></html>"
        
        truncatedContent = self.epubContent.truncate(5)
        self.assertEqual(expectedContent, truncatedContent)
        
    def testAddFooter(self):
        expectedContent = "<html><head><meta http-equiv='Content-Type'"+ \
        "content='text/html;charset=utf-8' /></head><body>"+\
        "<h1>HTML Ipsum Presents </h1><p><strong>Pellentesque "+ \
        "habitant morbi tristique</strong> senectus et netus et malesuada"+ \
        "fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae," + \
        "ultricies eget, tempor sit amet, ante. Donec eu libero"+\
        "<div> this is the footer</div>"
        self.epubContent.addFooter(self.footer)
        self.assertEqual(expectedContent,self.epubContent.content)
        
    def testPrepareFooter(self):
        expectedFooter = "<br><br><br> <hr width=60%/><b>"+"<div> this is the"+\
        " footer</div>".encode('utf-8')+"</b></body></html>"
        
        self.assertEquals(expectedFooter, self.epubContent.
            prepareFooter(self.footer))
        
    def testSplitIntoWords(self):
        splittedContent = self.epubContent.splitIntoWords()
        expectedValue = self.epubContent.content.split()
        self.assertEqual(splittedContent, expectedValue)

def main():
    unittest.main()

if __name__ == '__main__':
    main()