from epub import epub
from components import components
import unittest
import os

class componentsTest(unittest.TestCase):
    
    def setUp(self):
        epubPath = "/home/liliana/Projects/publication/"
        htmlzPath = "/home/liliana/Projects/publication/"
        epubId = "15882"
        epubF = epub(epubPath, htmlzPath, epubId)
        excerpt = epubF.createEpubFile("excerpt")
        originalEpubFilesPath = "/home/liliana/Projects/publication/extraction"
        self.component = components(excerpt, originalEpubFilesPath, htmlzPath, epubId )
          
    def testAddMimeType(self):
        self.component.addMimeType()
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
