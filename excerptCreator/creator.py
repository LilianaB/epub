from epub import epub
from epubFiles import epubFiles
from epubContent import epubContent
from components import components

class creator:

    def __init__(self, epubPath, htmlzPath, name):
        self.epub = epub(epubPath, htmlzPath, name)
        self.epubFiles = None
        self.epubContent = None
        self.size = 0.2
        self.images = None
        
    def generateXhtmlExcerpt(self):
        try:
            self.epub.convertEpubToHTMLZ()
            self.epub.createFolderWithEpubFiles() 
            self.epubFiles = epubFiles(self.epub.htmlzExtractionPath)
            self.epubContent = epubContent(self.epubFiles.getEpubContent())
            excerptContent = self.generateExcerptContent()
            self.epubFiles.createHtmlFileWithExcerpt(excerptContent.content)
            self.__manipulateFiles(excerptContent)
        except Exception as e:
            print e
            print ("Unable to create HTML excerpt")
            return False
        else:
            print ("Successfully created excerpt in html format")
            return True
                     
    def generateExcerptContent(self):
        text = self.epubContent.generateExcerptContent(self.size)
        excerptContent = epubContent(text)
        self.__addCover(excerptContent)
        excerptContent.addDoctype()
        return excerptContent.addUtf8Encoding()
            
    def __addCover(self, excerptContent):
        if (self.epubFiles.hasCover()):
            excerptContent.addCover()
        
    def __manipulateFiles(self, excerptContent):
        try:
            self.__moveCoverToImagesFolder()
            self.__deleteUnusedFiles(excerptContent)
        except Exception as e:
            print e
            print "Problem manipulation files for html excerpt"
                   
    def __moveCoverToImagesFolder(self):
        self.epubFiles.moveCoverToimagesFolder()
    
    def __deleteUnusedFiles(self, excerptContent):
        self.__deleteUnusedImages(excerptContent)
        self.epubFiles.deleteEpubIndexFile()
    
    def __deleteUnusedImages(self, excerptContent):
        self.epubFiles.deleteEpubImages(self.__getUnusedImages(excerptContent))
        
    def __getUnusedImages(self, excerptContent):
        self.images = excerptContent.getImages()
        return set(self.epubContent.getImages()) - set(self.images)
        
    def generateEpubExcerpt(self):
        try:
            htmls = [self.epub.htmlzExtractionPath+"excerpt.xhtml"]
            files = [self.epub.htmlzExtractionPath+"excerpt.xhtml", self.epub.htmlzExtractionPath+"style.css"]
            self.epub.unzipEpub()
            epubExcerpt = self.epub.createEpubFile("excerpt")
            excerptComponents = components(epubExcerpt, self.epub.epubExtractionPath, self.epub.htmlzExtractionPath, self.epub.name)
            excerptComponents.addMimeType()
            excerptComponents.addMetaInfoContainerXml()
            excerptComponents.addNavegation()
            excerptComponents.addContentAndOpf(epub,htmls, files)
            excerptComponents.addImages(self.images)

        except Exception as e:
            print e
            print ("Unable to create excerpt in ePub format")
            return False
        else:
            print ("Successfully created excerpt in ePub format")
            return True
