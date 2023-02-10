import os
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
import logging 

os.chdir('C:/Users/USER/Desktop/pdf')  # PDF文件存放的位置
logging.Logger.propagate = False 
logging.getLogger().setLevel(logging.ERROR)  

def main():
    content = find_number_from_pdf('testset')
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(content)

def find_number_from_pdf(filename):
    
    search_number = input("Please enter a number: ")
    path = filename+".pdf"

    praser = PDFParser(open(path, 'rb'))

    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)
    doc.initialize()

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    content = ''
    for page in doc.get_pages():
        interpreter.process_page(page)                        

        layout = device.get_result()
                          
        for x in layout:
            if isinstance(x, LTTextBox):
                line_list = x.get_text().strip().split(' ')
                if line_list[1] == search_number:
                    print(x.get_text().strip())
                    content  = content + x.get_text().strip() + "\n"
    return content


if __name__ == "__main__":
    main()
