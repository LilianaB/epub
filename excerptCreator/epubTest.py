from epub import epub
import unittest
import os

class epubTests(unittest.TestCase):
    
    def setUp(self):
        self.epubPath = "/home/liliana/Projects/publication/"
        self.htmlzPath = "/home/liliana/Projects/publication/"
        self.epubId = "15882"
        self.epubExtractionPath = self.htmlzPath + self.epubId +"originalExtraction/"
        self.epub = epub(self.epubPath, self.htmlzPath, self.epubId)
          
    def testConvertEpubToHtmlz(self):
        self.epub.convertEpubToHTMLZ()
        self.assertTrue(os.path.isfile(self.htmlzPath+self.epubId+".htmlz"))
          
    def testCreateFolderWithEpubFiles(self):
        self.epub.createFolderWithEpubFiles()
        self.assertTrue(os.path.isdir(self.epub.htmlzExtractionPath))
        
    def testCreateEpubFile(self):
        epub = self.epub.createEpubFile("excerpt")
        self.assertTrue(os.path.isfile(self.epub.htmlzExtractionPath+"/excerpt.epub"))

    def testUnzipEpub(self):
        self.epub.unzipEpub()
        self.assertTrue(os.path.isdir(self.epubExtractionPath))    
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
