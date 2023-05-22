#%%
import pdfplumber
import PyPDF4
import re
import os
import sys
from typing import Callable, List, Tuple, Dict

from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv


class PDF:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.pages = []
        self.metadata = {}
        

    def parse_pdf(self) -> Tuple[List[Tuple[int, str]], Dict[str, str]]:
        """
        Extracts the title and text from each page of the PDF.

        :return: A tuple containing the title and a list of tuples with page numbers and extracted text.
        """
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        print('parsing pdf')
        self.metadata = extract_metadata_from_pdf(self.file_path)
        self.pages = extract_pages_from_pdf(self.file_path)

        return self.pages, self.metadata
    
    def extract_metadata_from_pdf(self) -> dict:
        filepath = self.file_path
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF4.PdfFileReader(pdf_file)  # Change this line
            metadata = reader.getDocumentInfo()
            return {
                "title": metadata.get("/Title", "").strip(),
                "author": metadata.get("/Author", "").strip(),
                "creation_date": metadata.get("/CreationDate", "").strip(),
            }
    
    def extract_pages_from_pdf(self) -> List[Tuple[int, str]]:
        """ 
        Extracts the text from each page of the PDF.

        :return: A list of tuples containing the page number and the extracted text.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with pdfplumber.open(file_path) as pdf:
            pages = []
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text.strip():  # Check if extracted text is not empty
                    pages.append((page_num + 1, text))
        return pages
# %%
