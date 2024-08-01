def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    
    downcase_book = file_contents.lower()
    char_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
        " ": 0
        }
    for char in downcase_book:
        for letter in char_dict:
            if letter == char:
                char_dict[letter] += 1

    words = file_contents.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    
    char_list = []
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})
    
    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)

    print("-- Begin report of books/Frankenstien.txt --")
    print(f"{wordcount} words found in the document")
    
    for dict in char_list:
        print(f'''The '{dict["char"]}' character was found {dict["num"]} times''')

    print("-- End report --")

main()
