# import required module
import os
from langchain_text_splitters import MarkdownHeaderTextSplitter
from pinecone import Pinecone
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as lang_pine


def upsert(path):
	f = open(path, 'r')
	md=f.read()
	headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
	markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)
	profile_splits = markdown_splitter.split_text(md)


# assign directory
directory = './'
print(directory)
# iterate over files in 
# that directory
for filename in os.scandir(directory):
	if filename.is_file():
		upsert(filename.path)

