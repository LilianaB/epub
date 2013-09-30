from creator import *
import sys

print sys.argv[1]
epubName = sys.argv[1]#"15882" 
epubPath = "/home/liliana/Projects/publication/"
htmlzPath = "/home/liliana/Projects/publication/"

excerptCreator = creator(epubPath,htmlzPath,epubName)
excerptCreator.generateXhtmlExcerpt()
excerptCreator.generateEpubExcerpt()
