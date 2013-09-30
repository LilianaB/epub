epub
====
This project is made with the purpose of generating an ePub excerpt from an
existing ePub file (epub version 2).

To achive this, first the original epub is transforme into and html file using
the command ebook_convert offered via Calibre.

Once the original ePub is transforme into and html file, the parsing starts.
For the moment the excerpt generated will containt 20% of the original content.

The project is conformed for the next files:
    * components.py
    * epubContent.py
    * epub.py
    * epubFiles.py
    * createExcerpt.py
    * xmlParser.py
    * creator.py
    * main.py

File descriptions:

---- components.py
    This class handles all the components of an epub (images, opf, ncx, mimeType).
    It is encharged of creating the components and to add them to the epub excerpt.
    
---- epubContent.py
    Handles the epub Content (html file containing the epub text). 
    Extracts the excerpt content from the original html file, 
    cleans and prepares the html for being added to the epub excerpt.

---- epub.py
    this class handles the epub files. Unzip epub, create htmlz from epub
    and create new epub files.
    
---- epubFiles.py
    this class manage the files contained inside an epub onces the are unzipped
    
---- xmlParser.py
    parse the xml files contained on and epub, also generate the xml for the
    epub excerpt based on the originals files.

---- creator.py
    call the right methods to create and html and epub exceprt

---- main.py
    executable file to call the creation of an epub excerpt
    To try this tool, adjust the path on the main file and pass as parameter the
    name of the epub file to be used.


    
    
