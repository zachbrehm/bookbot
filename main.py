def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        create_report(word_count, char_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def get_chars_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "count": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def create_report(word_count, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    chars_sorted = get_chars_sorted_list(char_dict)
    for item in chars_sorted:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    print("--- End report ---")

main()