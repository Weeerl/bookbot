def main():
    full_text = read_file()
    word_count = count_words(full_text)

    print(" ---| Begin report on books/frankenstein.txt |---\n")
    print(word_count, " words were found in the document.\n")
    print("List of characters and number of occurrences:")
    char_dict = unique_characters(full_text)
    print_characters(char_dict)
    print("\n---| End of report |---")

def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def unique_characters(text):
    # Create empty dictionary for characters
    char_dict = {}
    # Loop over characters in text
    for char in text:
        char = char.lower()
        # For each character, if not in dictionary: add key to dictionary. Else: ignore
        if char not in char_dict:
            char_dict[char] = 0
        else:
            pass
        # Then dictionary value +1
        char_dict[char] += 1
        #print("New count of ", char, ": ", char_dict[char])
    return(char_dict)

def print_characters(dict):
    for k in dict:
        if k.isalpha():
            print("The\'", k, "\'character was found ", dict[k], " times.")

main()