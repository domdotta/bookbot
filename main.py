def character_count(file_contents):
    lower_string = file_contents.lower()
    char_dict = {}
    for char in lower_string:
        if char.isalpha():  # Only count alphabetic characters!
            if char in char_dict:
                char_dict[char] = char_dict[char] +1
            else:
                char_dict[char] = 1
    return char_dict

def wordcount(file_contents):
    words = file_contents.split()
    wordcount = len(words)
    return wordcount

def char_seperation(char_dict, word_count, file_name):
    # Print beginning of report
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()

    # Sort and display character counts
    char_seper = list(char_dict.items())
    char_seper.sort(key=lambda item: item[1], reverse=True)

    for char, count in char_seper:
        message = f"The '{char}' character was found {count} times"
        print(message)

    # Print end of report
    print("--- End report ---")

def main():
    # Specify file name
    file_name = "books/frankenstein.txt"

    # Read file and process contents
    with open(file_name) as f:
        file_contents = f.read()
        word_count = wordcount(file_contents)
        char_dict = character_count(file_contents)

        # Call char_seperation to print the report
        char_seperation(char_dict, word_count, file_name)

if __name__ == "__main__":
    main()
