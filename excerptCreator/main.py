from creator import creator
import sys

epubName = sys.argv[1]  #name of epub file without the extension (.epub)
epubPath = "/home/liliana/Projects/publication/"  #path to the epub file
htmlzPath = "/home/liliana/Projects/publication/" #path where the epub excerpt will be save

excerptCreator = creator(epubPath,htmlzPath,epubName)
excerptCreator.generateXhtmlExcerpt()
excerptCreator.generateEpubExcerpt()
