import zipfile
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
import os
ET.register_namespace('', 'http://some.namespace')

class epubXml:

    def __init__(self, epubExtractionPath, name, filename):
        self.epubExtraction = epubExtractionPath
        self.opfPath = epubExtractionPath +"OEBPS/"+filename
        self.tree = None
        self.root = None

    def readOpfRoot(self):
        self.tree = ET.parse(self.opfPath)
        self.root = self.tree.getroot()

    def clearElement(self,name):
        element = self.root.findall('{http://www.idpf.org/2007/opf}'+name)
        element[0].clear()
        
    def deleteElement(self,name):
        manifest = self.root.findall('{http://www.idpf.org/2007/opf}'+name)
        self.root.remove(manifest[0])
    
    def getElement(self,name):
        element = self.root.findall('{http://www.idpf.org/2007/opf}'+name)
        return element[0]

    def createElement(self, name):
        return Element(name)
        
    def createElementSpine(self):
        information = {'toc':"ncx"}
        return Element("spine", information)
        
        return Element(name)
    
    def appendElement(self, element):
        self.root.append(element)
    
    def addXhtmlToManifest(self, manifestElement, id, href):
        itemInformation = {'id':'item_%s' % (id), 'href': href, 'media-type':"application/xhtml+xml"}
        SubElement(manifestElement, "ns0:item", itemInformation)
        
    def addTocToManifest(self, manifestElement):
        itemInformation = {'id':"ncx", 'href': "toc.ncx", 'media-type':"application/x-dtbncx+xml"}
        SubElement(manifestElement, "ns0:item", itemInformation)
        
    def addStyleToManifest(self, manifestElement):
        itemInformation = {'id':"template-css", 'href': "style.css", 'media-type':"text/css"}
        SubElement(manifestElement, "ns0:item", itemInformation)
        
    def addItemsToManifest(self, manifestElement, htmls):
        for i, html in enumerate(htmls):
            basename = os.path.basename(html)
            self.addXhtmlToManifest(manifestElement, i, basename)
        self.addStyleToManifest(manifestElement)
        self.addTocToManifest(manifestElement)
        
    def getRoot(self):
        string = ET.tostring(self.root)
        return string
    
    def addXhtmlToSpine(self, spineElement, id):
        itemInformation = {'idref':'item_%s' % (id), 'linear':'yes'}
        SubElement(spineElement, "ns0:itemref", itemInformation)
        
    def addItemsToSpine(self, spine, htmls):
        for i, html in enumerate(htmls):
            self.addXhtmlToSpine(spine, i)
                      
    def addManifest(self, htmls):
        self.clearElement("manifest")
        elementManifest = self.getElement("manifest")
        self.addItemsToManifest(elementManifest, htmls)
        
    def addSpine(self, htmls):
        self.clearElement("spine")
        spine = self.getElement("spine")
        spine.attrib["toc"] = "ncx"
        self.addItemsToSpine(spine, htmls)

    def getNavElement(self):
        manifest = self.root.findall('{http://www.daisy.org/z3986/2005/ncx/}navMap')
        return manifest[0]
          
    def clearNavMap(self, name):
        manifest = self.root.findall('{http://www.daisy.org/z3986/2005/ncx/}'+name)
        manifest[0].clear()
        
    def addNavegationPoint(self):
        nav = self.getNavElement()
        information = {'id':'navpoint-1', 'playOrder':'1'}
        point = SubElement(nav, "ns0:navPoint", information)
        level = SubElement(point, "ns0:navLabel")
        text = SubElement(level, "ns0:text")
        text.text = "Content"
        info = {'src':'excerpt.xhtml'}
        point = SubElement(point, "ns0:content", info)
        
        
        
        
        
