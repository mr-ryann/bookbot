from stats import count_words,character_count,sorted_dict
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        string = file.read()
        return string
       
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path=sys.argv[1]
    string=get_book_text(file_path)
    count=count_words(string)
    dict=character_count(string)
    s_dict=sorted_dict(dict)
    
    print('='*12+''+'BOOKBOT'+''+'='*12)
    print(f'Analyzing book found at {file_path}...')
    print('-'*11+''+'Word Count'+''+'-'*11)
    print(f'Found {count} total words')
    print('-'*7+''+'Character Count'+''+'-'*7)
    for x in s_dict:
        print(f'{x["char"]}: {x["num"]}')
    print('='*13+''+'END'+''+'='*13)
main()
