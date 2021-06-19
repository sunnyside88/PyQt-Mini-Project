import fnmatch
from win32com.client import Dispatch
from PyPDF2 import PdfFileReader
import os
class PageCounter:
    @classmethod
    def count_pdf(cls):
        print("Counting PDF....")
