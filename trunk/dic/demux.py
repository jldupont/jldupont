import sys

class demux(object):
    
    fileNameTpl = "dic_%s.csv"
    
    def __init__(self):
        self.files = {}
        
    def write(self, keyword, lang, type):
        if (lang not in self.files[lang]):
            self.openFile(lang)
            
            
    def openFile(self, lang):
        self.files[lang] = open( self.fileNameTpl % lang, "w")

    def closeFiles(self):
        for file in self.files:
            file.close()