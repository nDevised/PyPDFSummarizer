import PyPDF2
class PDFtoText:

    def getTextOutput(file_path):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extract_text()

            output_path = 'path/to/output/text_file.txt'
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
