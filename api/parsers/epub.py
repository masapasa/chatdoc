from fastapi import UploadFile
from langchain.document_loaders.epub import UnstructuredEPubLoader

from .common import process_file


def process_epub(file: UploadFile, enable_summarization, user, user_openai_api_key):
    return process_file(file, UnstructuredEPubLoader, ".epub", enable_summarization, user, user_openai_api_key)
