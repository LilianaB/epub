from creator import *

epubPath = "/home/lbarrios/Projects/publications/"
htmlzPath = "/home/lbarrios/Projects/publications/"
epubId = "krauter"

excerptCreator = creator(epubPath,htmlzPath,epubId)
excerptCreator.generateXhtmlExcerpt()

excerptCreator.generateEpubExcerpt()
