def search_word():

    file_path = input("Enter the file path : ")
    word = input("Enter the word to search : ")

    content = open(file_path).read()

    if word in content:
        print(f"'{word}' Founf in the file.")

    else:
        print(f"'{word}' NOT found in the file.")

search_word()