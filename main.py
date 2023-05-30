import os
import fitz

directory = r'C:\Users\RogerYampang\Downloads'
pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
pdf_files.sort()
print('List of all pdfs:')
for file in pdf_files:
    print(file)
def search_pdf_document(directory, search_item):
    for file_name in os.listdir(directory):
        if not file_name.endswith('.pdf'):
            continue
        file_path = os.path.join(directory, file_name)
        with fitz.open(file_path) as doc:
            found_pages = []
            for page_num, page in enumerate(doc, 1):
                text = page.get_text()
                if search_item in text:
                    found_pages.append(page_num)
            if found_pages:
                print(f'Found match in {file_name}, pages: {", ".join(map(str, found_pages))}')

search_item = "Frankfurt"
print('\n')
print('Results:')
search_pdf_document(directory,search_item)