def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f'--- Begin report of books/frankenstein.txt ---')
        print(f"{len(words)} words found in the document")
        print("")
        number_of_characters(file_contents)
        print("--- End of report ---")

def number_of_characters(book):
    book = book.lower()
    
    char_count = {}
    
    for char in book:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    sort_dictionary(char_count)

def sort_dictionary(dictionary):
    for key, value in sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True):
        print(f"The '{key}' character was found {value} times")

main()