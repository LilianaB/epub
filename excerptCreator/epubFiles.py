# -*- coding: ISO-8859-1 -*-
import os
import zipfile
import logging
import shutil
from django.utils import text, html


class epubFiles:
    
    def __init__(self,pathToFiles):
        self.pathToFiles = pathToFiles
        
    def getIndexContent(self):
        content = ""
        f = open(self.pathToFiles+"index.html", 'r')
        content += f.read()
        content += "\n"
        f.close()
        return content
        
    def getEpubContent(self):
        try:
            return self.getIndexContent()
        except IOError:
            print ('Reading epub '+self.pathToFiles+"index.html")
            
    def moveCoverToimagesFolder(self):
        if os.path.isfile(self.pathToFiles+"cover.jpg"):
            shutil.move(self.pathToFiles+"cover.jpg", self.pathToFiles+"images/cover.jpg")
    
    def hasCover(self):
        return os.path.isfile(self.pathToFiles+"images/cover.jpg")
        
    def createHtmlFileWithExcerpt(self, excerpt):
        try:
            with open(self.pathToFiles+"excerpt.xhtml", "w") as f:
                f.write(excerpt)
        except IOError:
            print ( "Error: can\'t find file or read data")

    def deleteEpubIndexFile(self):
        try:
            os.remove(self.pathToFiles+"index.html")
        except OSError, e:
            print ( "Error: can\'t delete index.html file")
            
    def deleteEpubImages(self, images):
        for image in images:
            try:
                os.remove(self.pathToFiles+"/images/"+image)
            except OSError, e:
                print ("Error: can\'t delete image file"+ image)
        
