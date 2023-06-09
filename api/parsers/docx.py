from fastapi import UploadFile
from langchain.document_loaders import Docx2txtLoader

from .common import process_file


def process_docx(file: UploadFile, enable_summarization, user, user_openai_api_key):
    return process_file(file, Docx2txtLoader, ".docx", enable_summarization, user, user_openai_api_key)
