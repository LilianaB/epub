import zipfile
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
import os

class xmlParser:

    def __init__(self, filePath):
        self.tree = ET.parse(filePath)
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

    def appendElement(self, element):
        self.root.append(element)
        
    def getRoot(self):
        string = ET.tostring(self.root)
        return string
                      
    def configureManifest(self, htmls):
        self.clearElement("manifest")
        elementManifest = self.getElement("manifest")
        self.__addItemsToManifest(elementManifest, htmls)

    def __addItemsToManifest(self, manifestElement, htmls):
        for i, html in enumerate(htmls):
            basename = os.path.basename(html)
            self.__addXhtmlToManifest(manifestElement, i, basename)
        self.__addStyleToManifest(manifestElement)
        self.__addTocToManifest(manifestElement)
        
    def __addXhtmlToManifest(self, manifestElement, id, href):
        itemInformation = {'id':'item_%s' % (id), 'href': href, 'media-type':"application/xhtml+xml"}
        SubElement(manifestElement, "ns0:item", itemInformation)

    def __addTocToManifest(self, manifestElement):
        itemInformation = {'id':"ncx", 'href': "toc.ncx", 'media-type':"application/x-dtbncx+xml"}
        SubElement(manifestElement, "ns0:item", itemInformation)
        
    def __addStyleToManifest(self, manifestElement):
        itemInformation = {'id':"template-css", 'href': "style.css", 'media-type':"text/css"}
        SubElement(manifestElement, "ns0:item", itemInformation)
        
    def configureSpine(self, htmls):
        self.clearElement("spine")
        spine = self.getElement("spine")
        spine.attrib["toc"] = "ncx"
        self.__addItemsToSpine(spine, htmls)

    def __addItemsToSpine(self, spine, htmls):
        for i, html in enumerate(htmls):
            self.__addXhtmlToSpine(spine, i)
            
    def __addXhtmlToSpine(self, spineElement, id):
        itemInformation = {'idref':'item_%s' % (id), 'linear':'yes'}
        SubElement(spineElement, "ns0:itemref", itemInformation)
        
    def configureNavegationPoint(self):
        self.__clearNavMap()
        nav = self.__getNavMapElement()
        information = {'id':'navpoint-1', 'playOrder':'1'}
        point = SubElement(nav, "ns0:navPoint", information)
        level = SubElement(point, "ns0:navLabel")
        text = SubElement(level, "ns0:text")
        text.text = "Content"
        info = {'src':'excerpt.xhtml'}
        point = SubElement(point, "ns0:content", info)
        
    def __getNavMapElement(self):
        manifest = self.root.findall('{http://www.daisy.org/z3986/2005/ncx/}navMap')
        return manifest[0]
          
    def __clearNavMap(self):
        manifest = self.root.findall('{http://www.daisy.org/z3986/2005/ncx/}navMap')
        manifest[0].clear()
