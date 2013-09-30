# -*- coding: ISO-8859-1 -*-
#Extract new book
#zipfile.ZipFile(filepath).extractall(path=self.cache_path)
#Set permissions
#os.system("chmod 700 "+self.cache_path)

#Extract new book
#zipfile.ZipFile(filepath).extractall(path=self.cache_path)
#Set permissions
#os.system("chmod 700 "+self.cache_path)
from epubFiles import *
import unittest
import os

class epubFilesTests(unittest.TestCase):
    
    def setUp(self):
        self.pathToEpubFiles = "/home/liliana/Projects/publication/15882/"
        self.epubFiles = epubFiles(self.pathToEpubFiles)
        self.excerpt = "<html><head><meta http-equiv='Content-Type'"+ \
        "content='text/html;charset=utf-8' /><link href='style.css' "+ \
        "rel='stylesheet' type='text/css' /></head><body>"+\
        "<p class='body-ohne-ohne-abstand-nach-oben'>"+\
        "<span>Die Menschen dieses Landes wachsen wieder zusammen. Doch ich,"+\
        "denke es werden noch ein paar Jahre vergehen,bis wir uns auch wieder"+\
        "zusammengehorig fühlen werden.</span></p></div></body></html>"
        
    def testGetEpubContent(self):
        content = self.epubFiles.getEpubContent()
        self.assertIsNotNone(content)
        self.assertIsInstance(content, str)
        
    def testHasCover(self):
        self.epubFiles.moveCoverToimagesFolder()
        self.assertTrue(self.epubFiles.hasCover())
        
    def testCreateHtmlFileWithExcerpt(self):
        self.epubFiles.createHtmlFileWithExcerpt(self.excerpt)
        self.assertTrue(os.path.isfile(self.pathToEpubFiles+"excerpt.xhtml"))
        
    @unittest.skip("demonstrating skipping") 
    def testDeleteEpubIndexFile(self):
        self.epubFiles.deleteEpubIndexFile()
        self.assertFalse(os.path.isfile(self.pathToEpubFiles+"excerpt.xhtml"))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
