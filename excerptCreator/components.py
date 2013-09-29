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
            path = self.self.htmlzFilesPath+'/images/'+image
            basename = os.path.basename(path)
            if os.path.isfile(path):
                self.excerpt.write(path, 'OEBPS/images/'+basename)

    def addContentAndOpf(self, epub, htmls, files):
        for i, f in enumerate(files):
            basename = os.path.basename(f)
            self.__addHtml(epub,f,basename)
        string = self.prepareOpf(htmls)
        self.excerpt.writestr('OEBPS/Content.opf', '<?xml version="1.0" encoding="UTF-8" ?>\n'+string)
        
    def __addHtml(self, epub, html, basename):
        self.excerpt.write(html, 'OEBPS/'+basename)
        
    def prepareOpf(self, htmls):
        opfParser = xmlParser(self.originalEpubFilesPath+"OEBPS/content.opf")
        opfParser.configureManifest(htmls)
        opfParser.configureSpine(htmls)
        opfParser.deleteElement("guide")
        return opfParser.getRoot()

    def prepareNcx(self):
        ncxParser = xmlParser(self.originalEpubFilesPath+"OEBPS/toc.ncx")
        ncxParser.configureNavegationPoint()
        return ncxParser.getRoot()
