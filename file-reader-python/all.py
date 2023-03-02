import os
import pandas as pd
from PyPDF2 import PdfFileReader
import docx2txt
import io
import pefile

def read_file(file_path):

    file_extension = os.path.splitext(file_path)[1]

    if file_extension == '.pdf':
        with open(file_path, 'rb') as f:
            reader = io.BufferedReader(f)
            pdf = PdfFileReader(reader)
            contents = ''
            for page_num in range(pdf.getNumPages()):
                page = pdf.getPage(page_num)
                contents += page.extractText()
        return contents

    elif file_extension == '.xlsx' or file_extension == '.xls':
        df = pd.read_excel(file_path)
        return df

    elif file_extension == '.docx':
        contents = docx2txt.process(file_path)
        return contents

    elif file_extension == '.exe' or file_extension == '.dll':
        pe = pefile.PE(file_path)
        return pe.dump_info()

    else:
        with open(file_path, 'r') as f:
            contents = f.read()
        return contents
    