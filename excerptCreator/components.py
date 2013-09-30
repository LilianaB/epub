from xmlParser import xmlParser
import os
class components:

    def __init__(self, excerpt, originalEpubFilesPath, htmlzPath, name):
        self.originalEpubFilesPath = originalEpubFilesPath
        self.htmlzFilesPath = htmlzPath
        self.excerpt = excerpt
        self.epubName = name
        
    def addMimeType(self):
        self.excerpt.writestr("mimetype", "application/epub+zip")
        
    def addNavegation(self):
        self.excerpt.writestr("OEBPS/toc.ncx",'<?xml version="1.0" encoding="UTF-8" ?>\n'+self.prepareNcx())

    def addMetaInfoContainerXml(self):
        self.excerpt.writestr("META-INF/container.xml", 
	   '''<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
              <rootfiles>
                 <rootfile full-path="OEBPS/Content.opf" media-type="application/oebps-package+xml"/>
              </rootfiles>
           </container>''')
           
    def addImages(self, images):
        for image in images:
            path = self.htmlzFilesPath+'/images/'+image
            basename = os.path.basename(path)
            if os.path.isfile(path):
                self.excerpt.write(path, 'OEBPS/images/'+basename)

    def addContentAndOpf(self, epub, htmls, files, images):
        for i, f in enumerate(files):
            basename = os.path.basename(f)
            self.__addHtml(epub,f,basename)
        string = self.prepareOpf(htmls, images)
        self.excerpt.writestr('OEBPS/Content.opf', '<?xml version="1.0" encoding="UTF-8" ?>\n'+string)
        
    def __addHtml(self, epub, html, basename):
        self.excerpt.write(html, 'OEBPS/'+basename)
        
    def prepareOpf(self, htmls, images):
        opfPath = self.__getFilePath(".opf")
        print opfPath
        opfParser = xmlParser(opfPath)
        opfParser.configureManifest(htmls, images)
        opfParser.configureSpine(htmls)
        opfParser.deleteElement("guide")
        return opfParser.getRoot()

    def prepareNcx(self):
        ncxPath = self.__getFilePath(".ncx")
        print ncxPath
        ncxParser = xmlParser(ncxPath)
        ncxParser.configureNavegationPoint()
        return ncxParser.getRoot()
    
    def __getFilePath(self, fileType):
        path = self.originalEpubFilesPath
        for path, subdirs, files in os.walk(path):
            for x in files:
                if x.endswith(fileType) == True:
                    return os.path.join(path, x)
