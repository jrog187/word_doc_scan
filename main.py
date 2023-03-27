import os
import re
import docx2pdf
import fitz

def search_word_document(directory,search_term):
    #convert the word document to PDF
    for file_name in os.listdir(directory):
        if not file_name.endswith('.docx'):
            continue
        pdf_name = file_name[:-5] + '.pdf'
        docx2pdf.convert(os.path.join(directory,file_name), os.path.join(directory, pdf_name))

    #search through the pdf and extract the page number of each match
    for file_name in os.listdir(directory):
        if not file_name.endswith('.pdf'):
            continue
        with fitz.open(os.path.join(directory,file_name)) as doc:
            for page in doc:
                text = page.getText()
                for match in re.finditer(search_term,text):
                    print(f'Found match in {file_name}, paege {page.number + 1}')

#write the directory path of the word document you want to test
directory = r"C:\Users\roger\Downloads\urlaub_project_DE.docx"
search_term = 'apple'
search_word_document(directory, search_term)