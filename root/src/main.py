from utils.read_text import read_text_file
from utils.text_processing import preprocess_text
from utils.text_chunking import recursive_character_splitter
from utils.create_model import embed_store_and_model
from utils.questioning import ask_the_bot

def main(query):
    print('Generating response...')
    filepath_list = [
        'C:\\Users\\Akash\\Desktop\\GenAI\\CentraComm\\CentraComm\\data\\project\\alex_johnson.txt',
        'C:\\Users\\Akash\\Desktop\\GenAI\\CentraComm\\CentraComm\\data\\project\\emily_chen.txt',
        'C:\\Users\\Akash\\Desktop\\GenAI\\CentraComm\\CentraComm\\data\\project\\michael_reynolds.txt',
        'C:\\Users\\Akash\\Desktop\\GenAI\\CentraComm\\CentraComm\\data\\research\\alex_johnson.txt',
        'C:\\Users\\Akash\\Desktop\\GenAI\\CentraComm\\CentraComm\\data\\research\\jane_smith.txt',
        'C:\\Users\\Akash\\Desktop\\GenAI\\CentraComm\\CentraComm\\data\\research\\john_doe.txt',
        'C:\\Users\\Akash\\Desktop\\GenAI\\CentraComm\\CentraComm\\data\\training\\tasktracker.txt',
        'C:\\Users\\Akash\\Desktop\\GenAI\\CentraComm\\CentraComm\\data\\training\\virtualconnection.txt'
        ]
    
    chunk_collection = []

    for filepath in filepath_list:
        raw_text = read_text_file(filepath)
        processed_text = preprocess_text(raw_text)
        chunks = recursive_character_splitter(processed_text)
        chunk_collection.extend(chunks)
    
    qna_bot = embed_store_and_model(chunk_collection)
    result = ask_the_bot(query, qna_bot)
    print(result.strip())

if __name__ == '__main__':
    main(query='Whom can I contact regarding neural network concepts?')