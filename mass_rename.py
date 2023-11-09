import PyPDF2
import re
import os
directory_path = '/home/percy/Desktop/mom_coding/pdfs'

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    file_path = directory_path + '/' + filename
    pdfFileObj = open(file_path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pageObj = pdfReader.pages[0]

    # extracting text from page
    full_pdf_text = pageObj.extract_text()
    counsellor_name_list = re.findall("Counsellor:\n.*",full_pdf_text)
    for name in counsellor_name_list:
        counsellor_name = name[12:]
    pdfFileObj.close()
    
    new_filename = filename.strip(".pdf") + '-' + counsellor_name + ".pdf"
    print(new_filename)
    # Get the full file paths for the old and new names
    old_filepath = os.path.join(directory_path, filename)
    new_filepath = os.path.join(directory_path, new_filename)
    
    # Rename the file
    os.rename(old_filepath, new_filepath)
    print(f'Renamed: {filename} to {new_filename}'
