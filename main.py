from stats import count_words,character_count

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        string = file.read()
        return string
       
def main():
    file_path='books/frankenstein.txt'
    string=get_book_text(file_path)
    print(f'{count_words(string)} words found in the document.')
    print(character_count(string))
    
main()

