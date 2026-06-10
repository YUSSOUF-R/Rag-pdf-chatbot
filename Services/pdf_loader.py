import fitz
import os


class PDFLoader:
    def __init__(self, upload_folder="uploads"):
        self.upload_folder = upload_folder

    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text from a PDF file.
        """

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"File not found: {pdf_path}")

        text = ""

        try:
            pdf_document = fitz.open(pdf_path)

            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                text += page.get_text()

            pdf_document.close()

            return text

        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
