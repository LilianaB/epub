import zipfile
import logging
import subprocess
import os
import re
from epubXml import *
import time

class epub:
    
    def __init__(self, epubPath, htmlzPath, name):
        self.epubPath = epubPath + name + ".epub"
        self.htmlzPath = htmlzPath + name + ".htmlz"
        self.htmlzExtractionPath = htmlzPath + name +"/"
        self.epubExtractionPath = htmlzPath + name + "originalExtraction/"
        self.name = name
    
    def convertEpubToHTMLZ(self):
        try:
            subprocess.call(['ebook-convert', self.epubPath,self.htmlzPath])
        except:
            print ("Converting the epub to Htmlz")
            raise
        
    def createFolderWithEpubFiles(self):
        try:
            self.__unzipHtmlz()
        except:
            print ("Check if the "+self.epubPath+ \
                " exist or if calibre was able to convert it into HTMLZ.\n")
            raise
        
    def __unzipHtmlz(self):
        zipfile.ZipFile(self.htmlzPath). \
        extractall(self.htmlzExtractionPath)
        
    def unzipEpub(self):
        try:
            zipFile = zipfile.ZipFile(self.epubPath, 'r')
            for files in zipFile.namelist():
                zipFile.extract(files, self.epubExtractionPath)
            zipFile.close()
        except Exception as e:
            print e
            print "Problems while doing upzip of original epub files"
            raise
               
    def createEpubFile(self, name):
       return zipfile.ZipFile(self.htmlzExtractionPath+name+".epub", 'w')
        
