from epub import *
from epubFiles import *
from epubContent import *
import logging
import sys
from BeautifulSoup import BeautifulSoup

class excerpt:
    
    def __init__(self, epub, pathToEpubFiles, size, footer):
        self.epub = epub
        self.pathToEpubFiles = pathToEpubFiles
        self.size = size
        self.footer = footer
        self.images = None

    def createAndAddDetailsToExcerptContent(self, epubFilesClass, epubContentClass):
        excerptContent = epubContent(epubContentClass.generateExcerptContent(self.size))
        self.__moveCoverToImagesFolder(epubFilesClass)
        #self.__addFooter(excerptContent) this should be uncommented if you want to concatenate the footer to the excerpt.html
        self.__addCover(epubFilesClass, excerptContent)
        excerptContent.addDoctype()
        return excerptContent.addUtf8Encoding()
        
    def deleteUnusedFiles(self, epubFiles, epubContent, excerptContent):
        self.__deleteUnusedImages(epubFiles, epubContent, excerptContent)
        epubFiles.deleteEpubIndexFile()
        
    def generateHtmlExcerpt(self):
        epubFilesClass = None
        epubContentClass = None
        
        try:
            self.epub.convertEpubToHTMLZ()
            self.epub.createFolderWithEpubFiles()
            epubFilesClass = epubFiles(self.pathToEpubFiles)
            epubContentClass = epubContent(epubFilesClass.getEpubContent())
            excerptContent = self.createAndAddDetailsToExcerptContent(epubFilesClass, epubContentClass)
            epubFilesClass.createHtmlFileWithExcerpt(excerptContent.content)
            self.deleteUnusedFiles(epubFilesClass, epubContentClass, excerptContent)
        except Exception as e:
            print e
            print ("Unable to create HTML excerpt")
            return False
        else:
            print ("Successfully created excerpt in html format")
            return True
            
    def generateEpubExcerpt(self):
        try:
            htmls = [self.pathToEpubFiles+"excerpt.xhtml"]
            files = [self.pathToEpubFiles+"excerpt.xhtml", self.pathToEpubFiles+"style.css"]
            epub = self.epub.createEpub("excerpt")
            self.epub.addMimeType(epub)
            self.epub.addMetaInfoContainerXml(epub)
            self.epub.addNavegation(epub)
            self.epub.addContentAndOpf(epub,htmls, files)
            self.epub.addImages(epub, self.images)

        except Exception as e:
            print e
            print ("Unable to create excerpt in ePub format")
            return False
        else:
            print ("Successfully created excerpt in ePub format")
            return True         

    def __moveCoverToImagesFolder(self,epubFilesClass):
        epubFilesClass.moveCoverToimagesFolder()

    def __addFooter(self, excerptContent):
        excerptContent.addFooter(excerptContent.prepareFooter(self.footer))
            
    def __addCover(self, epubFilesClass, excerptContent):
        if (epubFilesClass.hasCover()):
            excerptContent.addCover()
        
    def __getUnusedImages(self, epubContent, excerptContent):
        self.images = excerptContent.getImages()
        return set(epubContent.getImages()) - set(self.images)
        
    def __deleteUnusedImages(self, epubFiles, epubContent, excerptContent):
        epubFiles.deleteEpubImages(self.__getUnusedImages(epubContent, excerptContent))
            
                
