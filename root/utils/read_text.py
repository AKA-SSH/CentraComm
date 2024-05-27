def read_text_file(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    
    return text