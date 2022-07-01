import fnmatch
from win32com.client import Dispatch
from PyPDF2 import PdfFileReader
import os
class PageCounter:
    @classmethod
    def count_pdf(cls, dir):
        dict = {}
        for index, f in enumerate(os.listdir(dir)):
            if f.endswith('.pdf') and os.path.isfile(os.path.join(dir, f)):
                file = open(os.path.join(dir, f), 'rb')
                reader = PdfFileReader(file)
                dict[f] = len(reader.pages)
        return dict
        

