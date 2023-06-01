from PyPDF2 import PdfReader


class PDFtoText:

    def getTextOutput(self,file_path):
        with open(file_path, 'rb') as file:
            with open(file_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                text = ''
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
