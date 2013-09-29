from epub import epub
from excerpt import excerpt

epubPath = "/home/liliana/Projects/publication/"
htmlzPath = "/home/liliana/Projects/publication/"
epubId = "15882"

epub = epub(pathToEpub,PathToHtmlz, extraction, name)
epubExcerpt = excerpt(epub, pathToEpubFiles, 0.2, footer)
value = epubExcerpt.generateHtmlExcerpt()

if value == False:
     print "Return value is False"

valueEpub = epubExcerpt.generateEpubExcerpt()
if valueEpub == False:
    print "Return value is False in epub"
