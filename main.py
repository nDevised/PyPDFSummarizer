from PDFtoText import *
from TextSummarizer import *
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')



def run():
    while True:
        file_path = input("Enter the location of the PDF document (or 'exit' to quit): ")
        if file_path.lower() == "exit":
            break

        try:
            pdf_to_txt = PDFtoText()
            text = pdf_to_txt.getTextOutput(file_path)
            summarizer = TextSummarizer(text)
            length_percent = float(input("Enter the desired summary length as a percentage (e.g., 30): "))/100
            summary = summarizer.summarize(length_percent)
            print("\nSummary:")
            print(summary)
            print()
        except FileNotFoundError:
            print("File not found. Please enter a valid file location.\n")
        except Exception as e:
            print("An error occurred:", str(e), "\n")

    print("Exiting the program.")

run()