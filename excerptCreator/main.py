from creator import *

epubPath = "/home/liliana/Projects/publication/"
htmlzPath = "/home/liliana/Projects/publication/"
epubId = "15882"

excerptCreator = creator(epubPath,htmlzPath,epubId)
excerptCreator.generateXhtmlExcerpt()

excerptCreator.generateEpubExcerpt()
