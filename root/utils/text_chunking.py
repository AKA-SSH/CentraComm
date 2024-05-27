from langchain_text_splitters import RecursiveCharacterTextSplitter

def recursive_character_splitter(text, chunk_size=512, chunk_overlap=64):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len, is_separator_regex=False)
    chunks = text_splitter.create_documents([text])
    
    return chunks